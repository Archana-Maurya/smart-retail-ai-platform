import os
from pathlib import Path

from dotenv import load_dotenv
from fastapi import APIRouter
from pydantic import BaseModel, Field

from azure.storage.blob import BlobServiceClient
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import (
    SearchIndex,
    SimpleField,
    SearchableField,
    SearchFieldDataType
)

from openai import OpenAI

load_dotenv()

router = APIRouter()

BASE_DIR = Path(__file__).resolve().parent.parent.parent

AZURE_STORAGE_ACCOUNT = os.getenv("AZURE_STORAGE_ACCOUNT", "")
AZURE_STORAGE_KEY = os.getenv("AZURE_STORAGE_KEY", "")
AZURE_CONTAINER_NAME = os.getenv("AZURE_CONTAINER_NAME", "smart-retail-data")

AZURE_SEARCH_ENDPOINT = os.getenv("AZURE_SEARCH_ENDPOINT", "")
AZURE_SEARCH_ADMIN_KEY = os.getenv("AZURE_SEARCH_ADMIN_KEY", "")
AZURE_SEARCH_INDEX = os.getenv("AZURE_SEARCH_INDEX", "smart-retail-index")

AZURE_OPENAI_BASE_URL = os.getenv("AZURE_OPENAI_BASE_URL", "")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY", "")
AZURE_OPENAI_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-4.1")


class SearchQuestion(BaseModel):
    question: str = Field(
        ...,
        json_schema_extra={
            "example": "What model is used for sales prediction?"
        }
    )


class ChatMessage(BaseModel):
    message: str = Field(
        ...,
        json_schema_extra={
            "example": "Explain Smart Retail Assistant project in 5 lines."
        }
    )


def get_blob_connection_string():
    return (
        "DefaultEndpointsProtocol=https;"
        f"AccountName={AZURE_STORAGE_ACCOUNT};"
        f"AccountKey={AZURE_STORAGE_KEY};"
        "EndpointSuffix=core.windows.net"
    )


def get_search_clients():
    credential = AzureKeyCredential(AZURE_SEARCH_ADMIN_KEY)

    index_client = SearchIndexClient(
        endpoint=AZURE_SEARCH_ENDPOINT,
        credential=credential
    )

    search_client = SearchClient(
        endpoint=AZURE_SEARCH_ENDPOINT,
        index_name=AZURE_SEARCH_INDEX,
        credential=credential
    )

    return index_client, search_client


def get_documents_for_search():
    knowledge_file = BASE_DIR / "rag" / "knowledge_base.txt"

    if knowledge_file.exists():
        knowledge_text = knowledge_file.read_text(encoding="utf-8")
    else:
        knowledge_text = "Smart Retail Assistant knowledge base is not available."

    documents = [
        {
            "id": "1",
            "source": "project_overview",
            "content": "Smart Retail Assistant is a retail analytics project for demand forecasting, customer question answering and anomaly detection."
        },
        {
            "id": "2",
            "source": "ml_model",
            "content": "The ML model predicts Sales using Quantity, Discount and Profit. The saved model file is models/superstore_pipeline_model.pkl."
        },
        {
            "id": "3",
            "source": "anomaly_detection",
            "content": "The anomaly detection module uses Isolation Forest with Sales, Quantity, Discount and Profit."
        },
        {
            "id": "4",
            "source": "rag_knowledge_base",
            "content": knowledge_text[:20000]
        }
    ]

    return documents


@router.get("/azure-status", summary="Azure Status")
def azure_status():
    return {
        "status": "success",
        "azure_blob_storage": {
            "storage_account_configured": bool(AZURE_STORAGE_ACCOUNT),
            "storage_key_configured": bool(AZURE_STORAGE_KEY),
            "container_name": AZURE_CONTAINER_NAME
        },
        "azure_ai_search": {
            "endpoint_configured": bool(AZURE_SEARCH_ENDPOINT),
            "admin_key_configured": bool(AZURE_SEARCH_ADMIN_KEY),
            "index_name": AZURE_SEARCH_INDEX
        },
        "azure_openai_foundry": {
            "base_url_configured": bool(AZURE_OPENAI_BASE_URL),
            "api_key_configured": bool(AZURE_OPENAI_API_KEY),
            "deployment_name": AZURE_OPENAI_DEPLOYMENT
        },
        "azure_web_app": {
            "component": "Azure App Service / Web App",
            "app_entry_point": "api.app:app"
        }
    }


@router.post("/azure-sync", summary="Azure Sync")
def azure_sync():
    try:
        uploaded_files = []

        if not AZURE_STORAGE_ACCOUNT or not AZURE_STORAGE_KEY:
            return {
                "status": "failed",
                "message": "Azure Storage credentials are missing in .env"
            }

        blob_service = BlobServiceClient.from_connection_string(
            get_blob_connection_string()
        )

        container_client = blob_service.get_container_client(AZURE_CONTAINER_NAME)

        try:
            container_client.create_container()
        except Exception:
            pass

        files_to_upload = [
            BASE_DIR / "data" / "processed" / "cleaned_superstore.csv",
            BASE_DIR / "models" / "superstore_pipeline_model.pkl",
            BASE_DIR / "models" / "anomaly_detection_model.pkl",
            BASE_DIR / "rag" / "knowledge_base.txt",
            BASE_DIR / "rag" / "vector_store.pkl"
        ]

        for file_path in files_to_upload:
            if file_path.exists():
                blob_name = str(file_path.relative_to(BASE_DIR)).replace("\\", "/")

                with open(file_path, "rb") as file:
                    container_client.upload_blob(
                        name=blob_name,
                        data=file,
                        overwrite=True
                    )

                uploaded_files.append(blob_name)

        if not AZURE_SEARCH_ENDPOINT or not AZURE_SEARCH_ADMIN_KEY:
            return {
                "status": "partial_success",
                "message": "Blob upload completed, but Azure AI Search credentials are missing.",
                "uploaded_files": uploaded_files
            }

        index_client, search_client = get_search_clients()

        fields = [
            SimpleField(
                name="id",
                type=SearchFieldDataType.String,
                key=True
            ),
            SearchableField(
                name="content",
                type=SearchFieldDataType.String
            ),
            SimpleField(
                name="source",
                type=SearchFieldDataType.String,
                filterable=True
            )
        ]

        index = SearchIndex(
            name=AZURE_SEARCH_INDEX,
            fields=fields
        )

        index_client.create_or_update_index(index)

        documents = get_documents_for_search()
        upload_result = search_client.upload_documents(documents=documents)

        return {
            "status": "success",
            "message": "Azure Blob Storage upload and Azure AI Search indexing completed successfully.",
            "blob_container": AZURE_CONTAINER_NAME,
            "uploaded_files": uploaded_files,
            "search_index": AZURE_SEARCH_INDEX,
            "documents_uploaded": len(documents),
            "search_upload_result": [str(item) for item in upload_result]
        }

    except Exception as error:
        return {
            "status": "failed",
            "message": str(error)
        }


@router.post("/azure-search-query", summary="Azure Search Query")
def azure_search_query(data: SearchQuestion):
    try:
        if not AZURE_SEARCH_ENDPOINT or not AZURE_SEARCH_ADMIN_KEY:
            return {
                "status": "failed",
                "message": "Azure AI Search credentials are missing in .env"
            }

        _, search_client = get_search_clients()

        results = search_client.search(
            search_text=data.question,
            top=3
        )

        matches = []

        for result in results:
            matches.append({
                "source": result["source"],
                "score": result["@search.score"],
                "content": result["content"]
            })

        return {
            "status": "success",
            "question": data.question,
            "index_name": AZURE_SEARCH_INDEX,
            "matches": matches
        }

    except Exception as error:
        return {
            "status": "failed",
            "message": str(error)
        }


@router.post("/azure-openai-chat", summary="Azure OpenAI Chat")
def azure_openai_chat(data: ChatMessage):
    try:
        if not AZURE_OPENAI_BASE_URL or not AZURE_OPENAI_API_KEY:
            return {
                "status": "failed",
                "message": "Azure OpenAI credentials are missing in .env"
            }

        client = OpenAI(
            api_key=AZURE_OPENAI_API_KEY,
            base_url=AZURE_OPENAI_BASE_URL
        )

        response = client.responses.create(
            model=AZURE_OPENAI_DEPLOYMENT,
            input=data.message,
            max_output_tokens=500
        )

        return {
            "status": "success",
            "deployment": AZURE_OPENAI_DEPLOYMENT,
            "response": response.output_text
        }

    except Exception as error:
        return {
            "status": "failed",
            "message": str(error),
            "hint": "Check Azure OpenAI base URL, API key and deployment name. They must belong to the same Foundry/OpenAI resource."
        }

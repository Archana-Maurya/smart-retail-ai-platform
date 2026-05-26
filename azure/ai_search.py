import os
from pathlib import Path
from dotenv import load_dotenv

from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import (
    SearchIndex,
    SimpleField,
    SearchableField,
    SearchFieldDataType
)

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

search_endpoint = os.getenv("AZURE_SEARCH_ENDPOINT")
search_key = os.getenv("AZURE_SEARCH_ADMIN_KEY")
index_name = os.getenv("AZURE_SEARCH_INDEX", "smart-retail-index")


def get_clients():
    credential = AzureKeyCredential(search_key)

    index_client = SearchIndexClient(
        endpoint=search_endpoint,
        credential=credential
    )

    search_client = SearchClient(
        endpoint=search_endpoint,
        index_name=index_name,
        credential=credential
    )

    return index_client, search_client


def create_index():
    index_client, _ = get_clients()

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
        name=index_name,
        fields=fields
    )

    index_client.create_or_update_index(index)

    print("Index ready:", index_name)


def load_documents():
    knowledge_file = BASE_DIR / "rag" / "knowledge_base.txt"

    if knowledge_file.exists():
        knowledge_text = knowledge_file.read_text(encoding="utf-8")
    else:
        knowledge_text = "Smart Retail Assistant project documentation."

    documents = [
        {
            "id": "1",
            "source": "project_overview",
            "content": "Smart Retail Assistant is a retail analytics project for demand forecasting, customer Q&A and anomaly detection."
        },
        {
            "id": "2",
            "source": "ml_model",
            "content": "The ML model predicts Sales using Quantity, Discount and Profit. The model file is superstore_pipeline_model.pkl."
        },
        {
            "id": "3",
            "source": "anomaly_detection",
            "content": "The anomaly detection module uses Isolation Forest with Sales, Quantity, Discount and Profit."
        },
        {
            "id": "4",
            "source": "knowledge_base",
            "content": knowledge_text[:20000]
        }
    ]

    return documents


def upload_documents():
    _, search_client = get_clients()

    documents = load_documents()

    result = search_client.upload_documents(documents=documents)

    print("Documents uploaded:", len(documents))

    for item in result:
        print(item)


def search_query(question):
    _, search_client = get_clients()

    results = search_client.search(
        search_text=question,
        top=3
    )

    print("Search question:", question)

    for result in results:
        print("Source:", result["source"])
        print("Score:", result["@search.score"])
        print("Content:", result["content"][:300])
        print("-" * 50)


def main():
    if not search_endpoint or not search_key:
        print("Azure AI Search credentials missing in .env")
        return

    create_index()
    upload_documents()
    search_query("What model is used for sales prediction?")


if __name__ == "__main__":
    main()

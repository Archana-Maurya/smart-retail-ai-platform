import os
from pathlib import Path
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

storage_account = os.getenv("AZURE_STORAGE_ACCOUNT")
storage_key = os.getenv("AZURE_STORAGE_KEY")
container_name = os.getenv("AZURE_CONTAINER_NAME", "smart-retail-data")

connection_string = (
    "DefaultEndpointsProtocol=https;"
    f"AccountName={storage_account};"
    f"AccountKey={storage_key};"
    "EndpointSuffix=core.windows.net"
)


def upload_file(container_client, file_path):
    blob_name = str(file_path.relative_to(BASE_DIR)).replace("\\", "/")

    with open(file_path, "rb") as file:
        container_client.upload_blob(
            name=blob_name,
            data=file,
            overwrite=True
        )

    print("Uploaded:", blob_name)


def main():
    if not storage_account or not storage_key:
        print("Azure Storage credentials missing in .env")
        return

    blob_service = BlobServiceClient.from_connection_string(connection_string)

    container_client = blob_service.get_container_client(container_name)

    try:
        container_client.create_container()
        print("Container created:", container_name)
    except Exception:
        print("Container already exists:", container_name)

    files_to_upload = [
        BASE_DIR / "data" / "processed" / "cleaned_superstore.csv",
        BASE_DIR / "models" / "superstore_pipeline_model.pkl",
        BASE_DIR / "models" / "anomaly_detection_model.pkl",
        BASE_DIR / "rag" / "knowledge_base.txt",
        BASE_DIR / "rag" / "vector_store.pkl"
    ]

    uploaded_count = 0

    for file_path in files_to_upload:
        if file_path.exists():
            upload_file(container_client, file_path)
            uploaded_count += 1
        else:
            print("Missing file:", file_path)

    print("Total uploaded files:", uploaded_count)


if __name__ == "__main__":
    main()

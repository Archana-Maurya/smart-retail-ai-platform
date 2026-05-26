import pandas as pd
from fastapi import APIRouter

from api.config import RAW_DATA_DIR, PROCESSED_DATA_DIR, CLEANED_DATA_PATH, COLLECTION_NAME
from api.database import get_collection
from api.logger import logger

router = APIRouter(
    prefix="/data-ingestion",
)


def get_first_csv_file():
    csv_files = list(RAW_DATA_DIR.glob("*.csv"))

    if not csv_files:
        return None

    return csv_files[0]


def make_columns_clean(df):
    df.columns = [
        column.strip().replace(" ", "_").replace("-", "_")
        for column in df.columns
    ]
    return df


def clean_data(df):
    df = make_columns_clean(df)

    for column in df.columns:
        if "Date" in column:
            df[column] = pd.to_datetime(df[column], errors="coerce")

    number_columns = df.select_dtypes(include=["int64", "float64"]).columns
    text_columns = df.select_dtypes(include=["object", "str"]).columns

    for column in number_columns:
        df[column] = df[column].fillna(df[column].median())

    for column in text_columns:
        df[column] = df[column].fillna("Unknown")

    df = df.drop_duplicates()

    return df


@router.post("", summary="Data Ingestion")
def data_ingestion():
    try:
        logger.info("Data ingestion started")

        dataset_path = get_first_csv_file()

        if dataset_path is None:
            return {
                "status": "failed",
                "message": "No CSV file found inside data/raw folder"
            }

        df = pd.read_csv(dataset_path, encoding="latin1")
        raw_rows = len(df)

        cleaned_df = clean_data(df)

        PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)
        cleaned_df.to_csv(CLEANED_DATA_PATH, index=False)

        mongodb_status = "not_connected"
        inserted_records = 0

        collection = get_collection(COLLECTION_NAME)

        if collection is not None:
            records = cleaned_df.astype(str).to_dict(orient="records")
            collection.delete_many({})

            if records:
                collection.insert_many(records)
                inserted_records = len(records)

            mongodb_status = "connected"

        logger.info("Data ingestion completed")

        return {
            "status": "success",
            "message": "Data ingestion completed successfully",
            "dataset_file": str(dataset_path),
            "raw_rows": raw_rows,
            "cleaned_rows": len(cleaned_df),
            "processed_file": str(CLEANED_DATA_PATH),
            "mongodb_status": mongodb_status,
            "inserted_records": inserted_records
        }

    except Exception as error:
        logger.error(f"Data ingestion failed: {error}")

        return {
            "status": "failed",
            "message": str(error)
        }


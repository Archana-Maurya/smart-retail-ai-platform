import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DATA_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DATA_DIR = BASE_DIR / "data" / "processed"
MODEL_DIR = BASE_DIR / "models"

CLEANED_DATA_PATH = PROCESSED_DATA_DIR / "cleaned_superstore.csv"
MODEL_PATH = MODEL_DIR / "superstore_pipeline_model.pkl"

MONGO_URI = os.getenv("MONGO_URI", "")
DATABASE_NAME = os.getenv("DATABASE_NAME", "smart_retail_db")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "retail_records")

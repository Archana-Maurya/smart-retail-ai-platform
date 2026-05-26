from pymongo import MongoClient

from api.config import MONGO_URI, DATABASE_NAME
from api.logger import logger

client = None
db = None


def get_database():
    global client, db

    if db is not None:
        return db

    if not MONGO_URI:
        logger.warning("MongoDB URI not found in .env")
        return None

    try:
        client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
        client.admin.command("ping")
        db = client[DATABASE_NAME]
        logger.info("MongoDB connected successfully")
        return db

    except Exception as error:
        logger.error(f"MongoDB connection failed: {error}")
        return None


def get_collection(collection_name):
    database = get_database()

    if database is None:
        return None

    return database[collection_name]

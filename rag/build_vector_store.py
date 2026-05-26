from pathlib import Path

import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

BASE_DIR = Path(__file__).resolve().parent.parent

KNOWLEDGE_FILE = BASE_DIR / "rag" / "knowledge_base.txt"
VECTOR_STORE_FILE = BASE_DIR / "rag" / "vector_store.pkl"


def split_text(text):
    chunks = []

    for part in text.split("\n\n"):
        clean_part = part.strip()

        if clean_part:
            chunks.append(clean_part)

    return chunks


def build_vector_store():
    if not KNOWLEDGE_FILE.exists():
        raise FileNotFoundError("knowledge_base.txt not found inside rag folder")

    text = KNOWLEDGE_FILE.read_text(encoding="utf-8")

    chunks = split_text(text)

    vectorizer = TfidfVectorizer(stop_words="english")

    vectors = vectorizer.fit_transform(chunks)

    vector_store = {
        "chunks": chunks,
        "vectorizer": vectorizer,
        "vectors": vectors
    }

    joblib.dump(vector_store, VECTOR_STORE_FILE)

    return {
        "message": "Vector store created successfully",
        "chunks": len(chunks),
        "file": str(VECTOR_STORE_FILE)
    }


if __name__ == "__main__":
    result = build_vector_store()
    print(result)

import joblib
from sklearn.metrics.pairwise import cosine_similarity

from rag.build_vector_store import VECTOR_STORE_FILE, build_vector_store


def load_vector_store():
    if not VECTOR_STORE_FILE.exists():
        build_vector_store()

    return joblib.load(VECTOR_STORE_FILE)


def search_documents(question, top_k=3):
    vector_store = load_vector_store()

    chunks = vector_store["chunks"]
    vectorizer = vector_store["vectorizer"]
    vectors = vector_store["vectors"]

    question_vector = vectorizer.transform([question])

    scores = cosine_similarity(question_vector, vectors).flatten()

    best_indexes = scores.argsort()[::-1][:top_k]

    results = []

    for index in best_indexes:
        results.append({
            "score": round(float(scores[index]), 4),
            "content": chunks[index]
        })

    return results

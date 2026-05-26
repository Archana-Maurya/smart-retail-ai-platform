from fastapi import APIRouter
from pydantic import BaseModel, Field

from api.logger import logger
from rag.search import search_documents

router = APIRouter(
    prefix="/document-search"
)


class SearchInput(BaseModel):
    question: str = Field(
        ...,
        json_schema_extra={
            "example": "What is the ML model used in this project?"
        }
    )


def choose_best_answer(question, results):
    question = question.lower()

    if not results:
        return "No relevant answer found."

    if "model" in question or "prediction" in question or "ml" in question:
        for result in results:
            content = result["content"].lower()
            if "model" in content or "random forest" in content or "prediction" in content:
                return result["content"]

    if "dataset" in question or "data" in question:
        for result in results:
            content = result["content"].lower()
            if "dataset" in content or "data" in content:
                return result["content"]

    if "agent" in question:
        for result in results:
            content = result["content"].lower()
            if "agent" in content:
                return result["content"]

    return results[0]["content"]


@router.post("", summary="RAG Vector Search")
def document_search(data: SearchInput):
    try:
        logger.info("RAG vector search request received")

        results = search_documents(data.question)

        answer = choose_best_answer(data.question, results)

        return {
            "status": "success",
            "question": data.question,
            "answer": answer,
            "results": results
        }

    except Exception as error:
        logger.error(f"RAG vector search failed: {error}")

        return {
            "status": "failed",
            "message": str(error)
        }

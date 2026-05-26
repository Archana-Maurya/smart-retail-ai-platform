from rag.search import search_documents

from agents.mcp import add_mcp_trace
from agents.data_agent import run_data_agent
from agents.document_agent import run_document_agent
from agents.ml_agent import run_ml_agent


def choose_agent(question):
    question = question.lower()

    ml_words = [
        "model",
        "prediction",
        "sales",
        "accuracy",
        "r2",
        "mae",
        "mse",
        "anomaly"
    ]

    data_words = [
        "data",
        "dataset",
        "mongodb",
        "clean",
        "ingestion",
        "pipeline"
    ]

    for word in ml_words:
        if word in question:
            return "ML Expert Agent"

    for word in data_words:
        if word in question:
            return "Data Analyst Agent"

    return "Document Assistant Agent"


def run_agent_system(question):
    mcp_trace = []

    add_mcp_trace(
        mcp_trace,
        sender="User",
        receiver="Orchestrator",
        message_type="question",
        content=question
    )

    selected_agent = choose_agent(question)

    add_mcp_trace(
        mcp_trace,
        sender="Orchestrator",
        receiver=selected_agent,
        message_type="agent_selection",
        content=f"{selected_agent} selected for this question"
    )

    search_results = search_documents(question)

    context = ""

    for result in search_results:
        context += result["content"] + "\n"

    add_mcp_trace(
        mcp_trace,
        sender="RAG Vector Store",
        receiver=selected_agent,
        message_type="context",
        content="Relevant context retrieved from vector store"
    )

    if selected_agent == "ML Expert Agent":
        answer = run_ml_agent(question, context)

    elif selected_agent == "Data Analyst Agent":
        answer = run_data_agent(question, context)

    else:
        answer = run_document_agent(question, context)

    add_mcp_trace(
        mcp_trace,
        sender=selected_agent,
        receiver="Orchestrator",
        message_type="answer",
        content=answer
    )

    return {
        "status": "success",
        "selected_agent": selected_agent,
        "question": question,
        "answer": answer,
        "rag_results": search_results,
        "mcp_trace": mcp_trace
    }

from langchain_core.prompts import PromptTemplate

from agents.llm_client import generate_agent_answer

DOCUMENT_AGENT_PROMPT = PromptTemplate.from_template(
    """
    You are a Document Assistant Agent.
    Answer questions using project documentation and RAG context.

    Question: {question}

    Context: {context}
    """
)


def run_document_agent(question, context):
    formatted_prompt = DOCUMENT_AGENT_PROMPT.format(
        question=question,
        context=context
    )

    fallback_answer = (
        "The Document Assistant Agent says: this Smart Retail Assistant project "
        "contains APIs for data ingestion, ML prediction, document search, agent interaction, "
        "Azure integration, data engineering and Power BI analytics."
    )

    if context:
        fallback_answer = fallback_answer + " Relevant context: " + context[:500]

    answer = generate_agent_answer(
        agent_name="Document Assistant Agent",
        question=question,
        context=context,
        formatted_prompt=formatted_prompt,
        fallback_answer=fallback_answer
    )

    return answer

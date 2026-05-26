from langchain_core.prompts import PromptTemplate

from agents.llm_client import generate_agent_answer

DATA_AGENT_PROMPT = PromptTemplate.from_template(
    """
    You are a Data Analyst Agent.
    Explain dataset, MongoDB and data pipeline details in simple language.

    Question: {question}

    Context: {context}
    """
)


def run_data_agent(question, context):
    formatted_prompt = DATA_AGENT_PROMPT.format(
        question=question,
        context=context
    )

    fallback_answer = (
        "The Data Analyst Agent says: this project uses Superstore retail data. "
        "The data ingestion API cleans the dataset, saves processed data and stores records in MongoDB. "
        "The data engineering pipeline also supports Raw to Staged to Curated analytics flow."
    )

    answer = generate_agent_answer(
        agent_name="Data Analyst Agent",
        question=question,
        context=context,
        formatted_prompt=formatted_prompt,
        fallback_answer=fallback_answer
    )

    return answer

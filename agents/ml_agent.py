from langchain_core.prompts import PromptTemplate

from agents.llm_client import generate_agent_answer

ML_AGENT_PROMPT = PromptTemplate.from_template(
    """
    You are an ML Expert Agent.
    Explain model training, prediction and anomaly detection in simple language.

    Question: {question}

    Context: {context}
    """
)


def run_ml_agent(question, context):
    formatted_prompt = ML_AGENT_PROMPT.format(
        question=question,
        context=context
    )

    fallback_answer = (
        "The ML Expert Agent says: the regression model predicts Sales using "
        "Quantity, Discount and Profit. The anomaly detection model uses Isolation Forest "
        "to detect unusual retail records using Sales, Quantity, Discount and Profit."
    )

    answer = generate_agent_answer(
        agent_name="ML Expert Agent",
        question=question,
        context=context,
        formatted_prompt=formatted_prompt,
        fallback_answer=fallback_answer
    )

    return answer

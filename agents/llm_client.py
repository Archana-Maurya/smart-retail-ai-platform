import os
from typing import Optional

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


def _normalize_azure_base_url(raw_url: str) -> str:
    """
    Supports both:
    - https://resource.openai.azure.com
    - https://resource.openai.azure.com/openai/v1
    - https://resource.services.ai.azure.com/openai/v1
    """
    url = raw_url.strip().rstrip("/")

    if url.endswith("/openai/v1"):
        return url + "/"

    if "/openai/" in url:
        return url + "/"

    return url + "/openai/v1/"


def generate_agent_answer(
    agent_name: str,
    question: str,
    context: str,
    formatted_prompt: str,
    fallback_answer: str
) -> str:
    """
    Generates a real AI response using Azure OpenAI.
    If Azure OpenAI is unavailable, returns a safe fallback answer
    so that /agent-interaction remains stable.
    """

    api_key = os.getenv("AZURE_OPENAI_API_KEY")
    base_url = (
        os.getenv("AZURE_OPENAI_BASE_URL")
        or os.getenv("AZURE_OPENAI_ENDPOINT")
    )
    deployment = (
        os.getenv("AZURE_OPENAI_DEPLOYMENT")
        or os.getenv("AZURE_OPENAI_MODEL")
        or "gpt-4.1"
    )

    if not api_key or not base_url or not deployment:
        return fallback_answer

    try:
        client = OpenAI(
            api_key=api_key,
            base_url=_normalize_azure_base_url(base_url),
            timeout=30
        )

        system_message = (
            f"You are {agent_name} in the Smart Retail AI Platform. "
            "Answer clearly, professionally, and only using the given project context. "
            "If the context is not enough, say what is known from the project."
        )

        user_message = f"""
Agent Prompt:
{formatted_prompt}

User Question:
{question}

Project/RAG Context:
{context[:5000]}
"""

        response = client.chat.completions.create(
            model=deployment,
            messages=[
                {
                    "role": "system",
                    "content": system_message
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ],
            temperature=0.2,
            max_tokens=500
        )

        ai_answer = response.choices[0].message.content.strip()

        return f"{agent_name} says: {ai_answer}"

    except Exception as error:
        return (
            fallback_answer
            + f" Azure OpenAI fallback used because live generation failed: {str(error)}"
        )

from fastapi import APIRouter
from pydantic import BaseModel, Field

from api.logger import logger
from agents.orchestrator import run_agent_system

router = APIRouter(
    prefix="/agent-interaction",
)


class AgentInput(BaseModel):
    question: str = Field(
        ...,
        json_schema_extra={
            "example": "Explain model performance"
        }
    )


@router.post("", summary="LangChain MCP Agent Interaction")
def agent_interaction(data: AgentInput):
    try:
        logger.info("LangChain MCP agent interaction request received")

        return run_agent_system(data.question)

    except Exception as error:
        logger.error(f"Agent interaction failed: {error}")

        return {
            "status": "failed",
            "message": str(error)
        }

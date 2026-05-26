from fastapi import FastAPI

from api.routes import data_ingestion
from api.routes import data_engineering
from api.routes import ml_prediction
from api.routes import document_search
from api.routes import agent_interaction
from api.routes import azure_cloud

app = FastAPI(
    title="Smart Retail Assistant",
    description="End-to-end Smart Retail AI Platform with FastAPI APIs, MongoDB ingestion, ML prediction, RAG document search, multi-agent AI interaction, Azure AI integration, Azure Data Engineering pipeline, and Power BI analytics.",
    version="1.0.0"
)

app.include_router(data_ingestion.router)
app.include_router(ml_prediction.router)
app.include_router(document_search.router)
app.include_router(agent_interaction.router)

app.include_router(azure_cloud.router)


app.include_router(data_engineering.router)




# Smart Retail AI Platform

Smart Retail AI Platform is an end-to-end Data + AI capstone project for retail analytics, sales prediction, anomaly detection, document search, multi-agent AI interaction, Azure AI integration, Azure Data Engineering, Azure App Service deployment, and Power BI visualization.

The project is based on a Smart Retail Assistant use case where a retail business can ingest data, predict sales, detect anomalies, search project knowledge, interact with role-based AI agents, and view insights through a published Power BI dashboard.

---

## Live Links

| Item | Link |
|---|---|
| GitHub Repository | https://github.com/Archana-Maurya/smart-retail-ai-platform |
| Live FastAPI Swagger URL | https://smart-retail-assistant-app-ftfmeme9b9a7bfcd.centralindia-01.azurewebsites.net/docs |

---

## Project Modules Status

| Module | Description | Final Status |
|---|---|---|
| Module A | FastAPI backend, REST APIs, MongoDB integration, pytest testing | Complete |
| Module B | Machine Learning prediction and anomaly detection | Complete |
| Module C | RAG, vector search, multi-agent interaction, MCP-style trace, Azure OpenAI agent response generation | Complete |
| Module D | Azure AI and cloud integration using Azure Blob Storage, Azure AI Search, Azure OpenAI / Azure AI Foundry | Complete |
| Module E | Azure Data Factory, Azure SQL, Raw to Staged to Curated pipeline, curated CSV/Parquet outputs | Complete |
| Module F | Power BI analytics dashboard with DAX measures, published report, and share proof | Complete |
| Module G | Final Azure App Service deployment with live Swagger and live agent endpoint | Complete |

---

## Final Deliverables Status

| Deliverable | Description | Status |
|---|---|---|
| Technical Documentation | Architecture, data flow, models, prompts, agents, APIs, deployment, security | Complete in this README |
| Working Code Repository | GitHub repository with clean folder structure | Complete |
| Deployment Diagram | Azure components and system interactions | Complete |
| Configuration Files | `.env.example`, `.gitignore`, `requirements.txt`, deployment requirements, GitHub Actions workflow | Complete |
| Power BI Report | Final analytics dashboard and published report proof | Complete |
| Demo Video | 5 to 10 minute project walkthrough | To be submitted separately |
| Reflection Note | Challenges, learnings, optimizations, future improvements | Complete: `reflection_note.md` |

---

## Tech Stack

- Python
- FastAPI
- MongoDB
- Pandas
- Scikit-learn
- Joblib
- Random Forest Regression
- Isolation Forest
- RAG / Vector Search
- Multi-Agent AI workflow
- Azure OpenAI / Azure AI Foundry
- Azure Blob Storage
- Azure AI Search
- Azure Data Factory
- Azure SQL Database
- Azure App Service
- GitHub Actions
- Power BI
- DAX
- Pytest

---

## Final Project Folder Structure

```text
smart_retail_project/
|
├── api/
│   ├── app.py
│   ├── config.py
│   ├── database.py
│   ├── logger.py
│   └── routes/
│       ├── data_ingestion.py
│       ├── ml_prediction.py
│       ├── document_search.py
│       ├── agent_interaction.py
│       ├── azure_cloud.py
│       └── data_engineering.py
|
├── agents/
│   ├── data_agent.py
│   ├── document_agent.py
│   ├── ml_agent.py
│   ├── orchestrator.py
│   ├── mcp.py
│   └── llm_client.py
|
├── rag/
│   ├── build_vector_store.py
│   ├── knowledge_base.txt
│   ├── search.py
│   └── vector_store.pkl
|
├── azure/
│   ├── ai_search.py
│   └── blob_upload.py
|
├── data/
│   ├── raw/
│   ├── processed/
│   ├── staged/
│   └── curated/
|
├── models/
│   ├── superstore_pipeline_model.pkl
│   ├── anomaly_detection_model.pkl
│   ├── random_forest_classifier.pkl
│   └── label_encoders.pkl
|
├── src/
│   ├── data_cleaning.py
│   ├── preprocessing_pipeline.py
│   ├── feature_engineering.py
│   ├── train_model.py
│   ├── evaluate_model.py
│   ├── predict.py
│   ├── anomaly_detection.py
│   ├── data_engineering_pipeline.py
│   └── powerbi_data_builder.py
|
├── powerbi/
│   ├── dashboard_kpis.csv
│   ├── model_outputs.csv
│   ├── anomaly_alerts.csv
│   ├── agent_insights.csv
│   └── smart_retail_dashboard.pbix
|
├── dashboard/
│   ├── executive_overview.png
│   ├── ml_model_outputs.png
│   ├── anomaly_agent_insights.png
│   ├── powerbi_publish_success.png
│   ├── powerbi_service_report.png
│   ├── powerbi_share_link_sent.png
│   ├── pytest_5_passed.png
│   ├── azure_webapp_swagger.png
│   ├── azure_agent_openai_live_test.png
│   └── azure_deployment_success.png
|
├── deployment/
│   └── requirements.txt
|
├── tests/
│   └── test_api.py
|
├── .github/
│   └── workflows/
│       └── main_smart-retail-assistant-app.yml
|
├── .env.example
├── .gitignore
├── README.md
├── reflection_note.md
└── requirements.txt
```

---

## Overall Project Architecture Diagram

```text
User / Evaluator
      |
      v
FastAPI Swagger UI / REST Client
      |
      v
FastAPI Backend APIs
      |
      |-- Data Ingestion API ----------> MongoDB
      |-- ML Prediction API -----------> Saved ML Model
      |-- Document Search API ---------> RAG Vector Store
      |-- Agent Interaction API -------> Multi-Agent System
      |                                      |
      |                                      |-- RAG Context Retrieval
      |                                      |-- Azure OpenAI Response Generation
      |                                      |-- MCP-style Trace
      |
      |-- Azure Cloud APIs ------------> Azure Blob Storage
      |                                  Azure AI Search
      |                                  Azure OpenAI / GPT Deployment
      |
      |-- Data Engineering API --------> Raw -> Staged -> Curated Pipeline
      |
      v
Power BI Dashboard
Executive KPIs | ML Outputs | Anomaly Alerts | Agent Insights
```

---

# Module A: Python Backend and APIs

Module A implements the backend using FastAPI. The backend exposes REST APIs for data ingestion, ML prediction, document search, agent interaction, Azure integration, and data engineering.

## Main FastAPI Entry Point

```text
api/app.py
```

## API Routes

| Endpoint | Method | Purpose |
|---|---|---|
| `/data-ingestion` | POST | Ingests and stores cleaned retail records |
| `/ml-prediction` | POST | Predicts sales using the trained ML model |
| `/document-search` | POST | Searches project knowledge using RAG/vector search |
| `/agent-interaction` | POST | Runs multi-agent AI interaction with RAG and MCP trace |
| `/azure-status` | GET | Checks Azure configuration status |
| `/azure-sync` | POST | Syncs files to Azure Blob Storage and Azure AI Search |
| `/azure-search-query` | POST | Queries Azure AI Search |
| `/azure-openai-chat` | POST | Tests Azure OpenAI chat generation |
| `/data-engineering-pipeline` | POST | Runs or validates data engineering outputs |

## Testing

Final API test execution passed successfully.

Proof screenshot:

```text
dashboard/pytest_5_passed.png
```

---

# Module B: Machine Learning and Anomaly Detection

Module B implements the machine learning layer for retail sales prediction and anomaly detection.

## ML Components

| Component | File / Folder |
|---|---|
| Data cleaning | `src/data_cleaning.py` |
| Preprocessing | `src/preprocessing_pipeline.py` |
| Feature engineering | `src/feature_engineering.py` |
| Model training | `src/train_model.py` |
| Model evaluation | `src/evaluate_model.py` |
| Prediction helper | `src/predict.py` |
| Anomaly detection | `src/anomaly_detection.py` |
| Saved model files | `models/` |

## Saved Models

```text
models/superstore_pipeline_model.pkl
models/anomaly_detection_model.pkl
models/random_forest_classifier.pkl
models/label_encoders.pkl
```

## ML Outputs Used in Power BI

```text
powerbi/model_outputs.csv
powerbi/anomaly_alerts.csv
```

---

# Module C: GenAI, RAG and Multi-Agent System

Module C implements RAG-based document search and a role-based multi-agent AI workflow.

## RAG Components

```text
rag/knowledge_base.txt
rag/vector_store.pkl
rag/search.py
rag/build_vector_store.py
```

## Agents

| Agent | File | Responsibility |
|---|---|---|
| Data Analyst Agent | `agents/data_agent.py` | Dataset, MongoDB, ingestion, and pipeline questions |
| Document Assistant Agent | `agents/document_agent.py` | Documentation, APIs, architecture, and project knowledge |
| ML Expert Agent | `agents/ml_agent.py` | ML model, prediction, evaluation, and anomaly detection |
| Orchestrator | `agents/orchestrator.py` | Selects the correct agent for the user question |
| MCP Trace | `agents/mcp.py` | Stores sender, receiver, message type, and content trace |
| Azure OpenAI Client | `agents/llm_client.py` | Generates real AI responses using Azure OpenAI |

## Module C Azure OpenAI Agent Enhancement

The multi-agent system was enhanced so that selected agents now generate real AI responses through Azure OpenAI.

Earlier, the agents used static fallback responses. The updated implementation now uses a common Azure OpenAI helper:

```text
agents/llm_client.py
```

The orchestrator still selects the correct role-based agent, RAG retrieves relevant project context, and the selected agent generates the final answer using Azure OpenAI.

## Updated Agent Flow

```text
User Question
      |
      v
Agent Orchestrator
      |
      v
RAG Vector Search
      |
      v
Selected Agent
      |
      v
Azure OpenAI
      |
      v
Final Answer + MCP Trace
```

## Agent API Response Includes

```text
selected_agent
Azure OpenAI generated answer
RAG search results
MCP-style trace
```

A fallback response is also included so that the `/agent-interaction` API remains stable if Azure OpenAI is unavailable.

## Live Agent AI Proof

The Azure deployed endpoint successfully generated an Azure OpenAI agent response with RAG results and MCP trace.

Proof screenshot:

```text
dashboard/azure_agent_openai_live_test.png
```

---

# Module D: Azure AI and Cloud Integration

Module D integrates the project with Azure AI and cloud services.

## Azure Services Used

| Azure Service | Usage |
|---|---|
| Azure Blob Storage | Stores project data/model/RAG artifacts and supports cloud sync |
| Azure AI Search | Provides cloud search index for project knowledge |
| Azure OpenAI / Azure AI Foundry | Generates cloud-based GenAI responses |
| Azure App Service | Hosts the deployed FastAPI backend |
| Azure Data Factory | Supports data engineering orchestration |
| Azure SQL Database | Stores staged/curated analytical data |

## Azure Helper Files

```text
azure/blob_upload.py
azure/ai_search.py
api/routes/azure_cloud.py
```

## Azure Cloud Endpoints

| Endpoint | Purpose |
|---|---|
| `GET /azure-status` | Checks Azure configuration status |
| `POST /azure-sync` | Uploads/syncs files to Azure Blob Storage and indexes documents |
| `POST /azure-search-query` | Queries Azure AI Search |
| `POST /azure-openai-chat` | Generates Azure OpenAI response |

---

## Azure Deployment Diagram

```text
User / Evaluator
      |
      v
Live FastAPI Swagger UI
      |
      v
Azure App Service / Web App
      |
      |-- FastAPI Backend
      |-- Data Ingestion API
      |-- ML Prediction API
      |-- Document Search API
      |-- Agent Interaction API
      |
      |-- MongoDB Atlas / MongoDB
      |-- Saved ML Models
      |-- RAG Vector Store
      |-- Multi-Agent System
      |-- Azure OpenAI
      |-- Azure Blob Storage
      |-- Azure AI Search
      |-- Azure Data Engineering Outputs
```

---

## Security Considerations

This project follows basic security practices for cloud credentials and deployment configuration.

### Environment Variables

Sensitive values are stored in environment variables instead of being hardcoded in source code.

Local development uses:

```text
.env
```

A safe sample file is included for submission:

```text
.env.example
```

The following values are configured through environment variables or Azure App Service App Settings:

```text
MONGO_URI
DATABASE_NAME
COLLECTION_NAME
AZURE_STORAGE_ACCOUNT
AZURE_STORAGE_KEY
AZURE_CONTAINER_NAME
AZURE_SEARCH_ENDPOINT
AZURE_SEARCH_ADMIN_KEY
AZURE_SEARCH_INDEX
AZURE_OPENAI_ENDPOINT
AZURE_OPENAI_BASE_URL
AZURE_OPENAI_API_KEY
AZURE_OPENAI_DEPLOYMENT
SCM_DO_BUILD_DURING_DEPLOYMENT
```

### GitHub Safety

The `.gitignore` file excludes local secrets and temporary folders:

```text
.env
venv/
__pycache__/
.pytest_cache/
*.pyc
```

### Azure Key Vault Recommendation

For production deployment, Azure Key Vault should be used to securely store and manage:

```text
MongoDB URI
Azure Storage Key
Azure AI Search Key
Azure OpenAI Key
Other production secrets
```

If any key is accidentally exposed, it should be regenerated immediately from the Azure Portal.

---

# Module E: Data Engineering Pipeline

Module E implements a data engineering pipeline using Azure Data Factory, Azure SQL Database, Azure Blob Storage style layers, and curated outputs.

## Pipeline Flow

```text
Raw Data
   |
   v
Staged Data
   |
   v
Curated Analytical Tables
   |
   v
CSV / Parquet Outputs
   |
   v
Power BI Analytics
```

## Data Layers

| Layer | Folder / Output |
|---|---|
| Raw | `data/raw/` |
| Processed | `data/processed/` |
| Staged | `data/staged/` |
| Curated | `data/curated/` |

## Curated Outputs

```text
data/curated/curated_region_summary.csv
data/curated/curated_category_summary.csv
data/curated/curated_monthly_summary.csv
data/curated/curated_region_summary.parquet
```

## Data Engineering API

```text
POST /data-engineering-pipeline
```

---

## Data Engineering Pipeline Diagram

```text
Superstore Raw CSV
        |
        v
Data Cleaning / Processing
        |
        v
Staged Superstore Data
        |
        v
Azure SQL / Curated Summary Logic
        |
        |-- Region-wise Sales and Profit
        |-- Category-wise Sales and Profit
        |-- Monthly Sales and Profit
        |
        v
Curated CSV / Parquet Outputs
        |
        v
Power BI Dashboard
```

---

# Module F: Analytics and Visualization

Module F implements Power BI analytics and visualization.

## Power BI Data Files

```text
powerbi/dashboard_kpis.csv
powerbi/model_outputs.csv
powerbi/anomaly_alerts.csv
powerbi/agent_insights.csv
```

## Power BI Report File

```text
powerbi/smart_retail_dashboard.pbix
```

## Dashboard Pages

| Page | Purpose |
|---|---|
| Executive Overview | Sales, profit, quantity, discount, records, region/category/monthly analysis |
| ML Model Outputs | Predicted sales, prediction error, top prediction errors, error category |
| Anomaly Alerts and Agent Insights | Anomaly count, anomaly rate, region trend, monthly trend, agent insights |

## DAX Measures

Power BI DAX measures are used for KPI and analytical calculations such as:

```text
Total Sales
Total Profit
Total Quantity
Average Discount
Total Records
Profit Margin
Average Predicted Sales
Average Prediction Error
Model Records
Total Anomaly Alerts
Anomaly Rate
Agent Insight Count
```

## Module F Publish Proof

The Power BI dashboard was successfully published to Power BI Service and share proof was captured.

Proof screenshots:

```text
dashboard/executive_overview.png
dashboard/ml_model_outputs.png
dashboard/anomaly_agent_insights.png
dashboard/powerbi_publish_success.png
dashboard/powerbi_service_report.png
dashboard/powerbi_share_link_sent.png
```

---

# Module G: Final Azure Deployment

Module G deploys the FastAPI backend to Azure App Service.

## Deployment Platform

```text
Azure App Service / Web App
Runtime: Python 3.11
Operating System: Linux
Deployment Source: GitHub Actions
```

## Live Swagger URL

```text
https://smart-retail-assistant-app-ftfmeme9b9a7bfcd.centralindia-01.azurewebsites.net/docs
```

## GitHub Actions Workflow

Azure App Service created the GitHub Actions workflow file:

```text
.github/workflows/main_smart-retail-assistant-app.yml
```

## Startup Command

```text
gunicorn -w 2 -k uvicorn.workers.UvicornWorker api.app:app --bind=0.0.0.0:8000 --timeout 600
```

## Deployment Proof Screenshots

```text
dashboard/azure_webapp_swagger.png
dashboard/azure_agent_openai_live_test.png
dashboard/azure_deployment_success.png
```

## Live Deployment Verification

The deployed cloud API was verified through Swagger UI. The `/agent-interaction` endpoint returned:

```text
status: success
selected_agent: ML Expert Agent
Azure OpenAI generated answer
RAG search results
MCP-style trace
```

---

# How to Run Locally

## 1. Create and activate virtual environment

```powershell
python -m venv venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\venv\Scripts\Activate.ps1
```

## 2. Install dependencies

```powershell
pip install -r requirements.txt
```

## 3. Create `.env`

Use `.env.example` as a template and add real credentials locally.

```text
.env.example
```

Do not push `.env` to GitHub.

## 4. Run FastAPI server

```powershell
python -m uvicorn api.app:app --reload
```

Open local Swagger:

```text
http://127.0.0.1:8000/docs
```

---

# How to Run Tests

```powershell
$env:PYTHONPATH = "C:\Users\Hp2\Desktop\smart_retail_project"
python -m pytest tests\test_api.py -v
```

Expected result:

```text
5 passed
```

Proof screenshot:

```text
dashboard/pytest_5_passed.png
```

---

# Final Submission Proof Files

## Dashboard Proof

```text
dashboard/executive_overview.png
dashboard/ml_model_outputs.png
dashboard/anomaly_agent_insights.png
```

## Power BI Publish Proof

```text
dashboard/powerbi_publish_success.png
dashboard/powerbi_service_report.png
dashboard/powerbi_share_link_sent.png
```

## Azure Deployment Proof

```text
dashboard/azure_webapp_swagger.png
dashboard/azure_agent_openai_live_test.png
dashboard/azure_deployment_success.png
```

## Testing Proof

```text
dashboard/pytest_5_passed.png
```

## Reflection Note

```text
reflection_note.md
```

---

# Final Project Status

```text
Module A: Complete
Module B: Complete
Module C: Complete with Azure OpenAI Agent Enhancement
Module D: Complete
Module E: Complete
Module F: Complete and Published
Module G: Complete and Deployed
```

The project is ready for final evaluation with GitHub repository, deployed Azure Web App, Power BI published report, reflection note, screenshots, and live Swagger API.

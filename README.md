# Smart Retail AI Platform

Smart Retail AI Platform is an end-to-end Data + AI capstone project built on the **Smart Retail Assistant** use case.  
It combines Python backend APIs, MongoDB, Machine Learning, RAG, multi-agent AI interaction, Azure cloud services, Azure Data Engineering, and Power BI analytics.

The project focuses on:

- demand forecasting
- sales prediction
- anomaly detection
- document question answering
- multi-agent AI interaction
- Azure cloud integration
- Raw to Staged to Curated data engineering
- Power BI dashboard reporting

---

## Project Description

The Smart Retail AI Platform is designed to solve retail business problems using Data Engineering, Machine Learning, GenAI, Azure Cloud, and Power BI.

The platform includes:

- FastAPI backend with REST APIs
- MongoDB integration for data storage
- ML model for sales prediction
- anomaly detection for unusual retail transactions
- RAG-based document search
- MCP-style multi-agent interaction
- Azure Blob Storage, Azure AI Search, and Azure OpenAI integration
- Azure Data Factory and Azure SQL data engineering pipeline
- Power BI dashboard with KPI cards, model outputs, anomaly trends, agent insights, and DAX measures

Dataset used:

```text
Sample - Superstore.csv
```

---

## Project Modules Status

| Module | Description | Status |
|---|---|---|
| Module A | FastAPI backend, REST APIs, MongoDB integration, pytest testing | Complete |
| Module B | Machine Learning prediction and anomaly detection | Complete |
| Module C | RAG, vector search, multi-agent interaction, MCP-style trace | Complete |
| Module D | Azure AI and cloud integration | Complete locally; Azure Web App deployment pending |
| Module E | Azure Data Factory, Azure SQL, Raw to Staged to Curated pipeline, Parquet output | Complete |
| Module F | Power BI analytics dashboard with DAX measures | Complete; publish/share attempt pending |

---

## Tech Stack

- Python
- FastAPI
- MongoDB
- Pandas
- Scikit-learn
- Joblib
- LangChain / RAG workflow
- Multi-Agent AI workflow
- Azure Blob Storage
- Azure AI Search
- Azure OpenAI / Azure AI Foundry
- Azure Data Factory
- Azure SQL Database
- Power BI
- DAX
- Pytest

---

## Project Folder Structure

```text
smart_retail_project/
|
|-- agents/
|   |-- __init__.py
|   |-- data_agent.py
|   |-- document_agent.py
|   |-- mcp.py
|   |-- ml_agent.py
|   |-- orchestrator.py
|
|-- api/
|   |-- app.py
|   |-- routes/
|       |-- agent_interaction.py
|       |-- azure_cloud.py
|       |-- data_engineering.py
|       |-- data_ingestion.py
|       |-- document_search.py
|       |-- ml_prediction.py
|
|-- azure/
|   |-- ai_search.py
|   |-- blob_upload.py
|
|-- data/
|   |-- raw/
|   |   |-- Sample - Superstore.csv
|   |   |-- superstore_adf_sql.csv
|   |-- processed/
|   |   |-- anomaly_detected_superstore.csv
|   |   |-- cleaned_superstore.csv
|   |   |-- feature_engineered_superstore.csv
|   |   |-- preprocessed_superstore.csv
|   |-- staged/
|   |   |-- staged_superstore_sample.csv
|   |-- curated/
|       |-- curated_category_summary.csv
|       |-- curated_monthly_summary.csv
|       |-- curated_region_summary.csv
|       |-- curated_region_summary.parquet
|
|-- deployment/
|   |-- requirements.txt
|
|-- models/
|   |-- anomaly_detection_model.pkl
|   |-- label_encoders.pkl
|   |-- random_forest_classifier.pkl
|   |-- superstore_pipeline_model.pkl
|
|-- powerbi/
|   |-- agent_insights.csv
|   |-- anomaly_alerts.csv
|   |-- dashboard_kpis.csv
|   |-- model_outputs.csv
|   |-- smart_retail_dashboard.pbix
|
|-- rag/
|   |-- __init__.py
|   |-- build_vector_store.py
|   |-- knowledge_base.txt
|   |-- search.py
|   |-- vector_store.pkl
|
|-- src/
|   |-- anomaly_detection.py
|   |-- data_cleaning.py
|   |-- data_engineering_pipeline.py
|   |-- evaluate_model.py
|   |-- feature_engineering.py
|   |-- powerbi_data_builder.py
|   |-- predict.py
|   |-- preprocessing_pipeline.py
|   |-- save_model.py
|   |-- train_model.py
|   |-- visualization.py
|
|-- tests/
|   |-- test_api.py
|
|-- .gitignore
|-- requirements.txt
|-- README.md
```

---

## Overall Project Architecture Diagram

```text
User / Evaluator
       |
       v
FastAPI Swagger UI
       |
       +--------------------+--------------------+----------------------+----------------------+----------------------+
       |                    |                    |                      |                      |
       v                    v                    v                      v                      v
Data Ingestion API    ML Prediction API    Document Search API    Agent Interaction API    Azure Cloud APIs
       |                    |                    |                      |                      |
       v                    v                    v                      v                      v
MongoDB Atlas       Saved ML Models       RAG Vector Store        Multi-Agent System       Azure Services
                                                                    |                     /      |       \
                                                                    v                    v       v        v
                                                               MCP-style Trace      Blob Storage AI Search Azure OpenAI
```

---

# Module A: Python Backend and APIs

Module A implements the backend layer of the Smart Retail AI Platform using **FastAPI**.

## Implemented Features

- Python-based backend using FastAPI
- REST API development
- MongoDB integration
- Swagger UI for API testing
- Pytest-based API testing

## Main API Files

```text
api/app.py
api/routes/data_ingestion.py
api/routes/ml_prediction.py
api/routes/document_search.py
api/routes/agent_interaction.py
api/routes/azure_cloud.py
api/routes/data_engineering.py
```

## REST APIs

| Endpoint | Purpose |
|---|---|
| `POST /data-ingestion` | Reads, cleans, processes, and stores Superstore data in MongoDB |
| `POST /ml-prediction` | Predicts sales using the trained ML model |
| `POST /document-search` | Performs RAG/vector search over project knowledge |
| `POST /agent-interaction` | Uses multi-agent orchestration with MCP-style trace |
| `POST /data-engineering-pipeline` | Verifies local Raw to Staged to Curated pipeline outputs |
| `GET /azure-status` | Checks Azure configuration status |
| `POST /azure-sync` | Uploads files to Azure Blob and indexes data in Azure AI Search |
| `POST /azure-search-query` | Queries Azure AI Search |
| `POST /azure-openai-chat` | Generates response using Azure OpenAI / GPT-4.1 |

## Database Used

- MongoDB Atlas

## Module A Verification

- FastAPI server runs successfully.
- Swagger UI opens successfully.
- MongoDB connection works.
- Data ingestion API processes 9994 records.
- API test cases pass using pytest.

---

# Module B: Machine Learning and Anomaly Detection

Module B implements the Machine Learning layer of the Smart Retail AI Platform.

## Implemented Features

- data cleaning
- feature engineering
- preprocessing pipeline
- model training
- model evaluation
- model persistence using Joblib
- anomaly detection

## Important Files

```text
src/data_cleaning.py
src/feature_engineering.py
src/preprocessing_pipeline.py
src/train_model.py
src/evaluate_model.py
src/save_model.py
src/predict.py
src/anomaly_detection.py
```

## Models Used

| Model | Purpose |
|---|---|
| Random Forest Regressor | Sales prediction |
| Random Forest Classifier | Classification support |
| Isolation Forest | Anomaly detection |

## Prediction Features

The sales prediction model uses:

- Quantity
- Discount
- Profit

## Saved Model Files

```text
models/superstore_pipeline_model.pkl
models/anomaly_detection_model.pkl
models/random_forest_classifier.pkl
models/label_encoders.pkl
```

## Module B Verification

- Model training completed successfully.
- Prediction API works successfully.
- Anomaly detection output generated.
- Model files are stored inside `models/`.
- Power BI uses model output data for ML visualization.

---

# Module C: GenAI, RAG and Multi-Agent System

Module C implements the GenAI and multi-agent part of the Smart Retail AI Platform.

## Implemented Features

- RAG knowledge base
- vector store creation
- document search
- multi-agent orchestration
- MCP-style structured trace
- agent-driven response generation

## Important Files

```text
rag/build_vector_store.py
rag/knowledge_base.txt
rag/search.py
rag/vector_store.pkl

agents/data_agent.py
agents/document_agent.py
agents/ml_agent.py
agents/mcp.py
agents/orchestrator.py
```

## Agents Implemented

| Agent | Purpose |
|---|---|
| Data Analyst Agent | Answers data, MongoDB, and pipeline-related questions |
| Document Assistant Agent | Answers project documentation and API-related questions |
| ML Expert Agent | Answers model training, prediction, and anomaly detection questions |

## RAG and Agent Flow

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
Relevant Context
      |
      v
Selected Agent
      |
      v
Final Answer + MCP Trace
```

## APIs

```text
POST /document-search
POST /agent-interaction
```

## Module C Verification

- Document search API returns relevant RAG results.
- Agent interaction API selects the correct agent.
- Agent response includes selected agent, answer, RAG context, and MCP trace.
- MCP-style trace is visible in API response.

---

# Module D: Azure AI and Cloud Integration

This module connects the Smart Retail AI Platform with Azure cloud services.

## Azure Components Used

1. **Azure Blob Storage**  
   Azure Blob Storage is used to store processed data, trained ML models, the RAG knowledge base, and vector store files.

   Uploaded files:
   - `data/processed/cleaned_superstore.csv`
   - `models/superstore_pipeline_model.pkl`
   - `models/anomaly_detection_model.pkl`
   - `rag/knowledge_base.txt`
   - `rag/vector_store.pkl`

2. **Azure AI Search**  
   Azure AI Search is used to create a cloud search index for project knowledge.

   Index name:
   - `smart-retail-index`

3. **Azure AI Foundry / Azure OpenAI**  
   Azure AI Foundry with GPT-4.1 is used for cloud-based GenAI response generation.

4. **Azure Web App / App Service**  
   Azure Web App is planned for FastAPI backend deployment.

   FastAPI entry point:
   - `api.app:app`

## Azure Helper Files

```text
azure/blob_upload.py
azure/ai_search.py
api/routes/azure_cloud.py
```

## Azure Deployment Diagram

```text
User / Evaluator
        |
        v
FastAPI Swagger UI
        |
        v
Azure Web App / FastAPI Backend
        |
        |---- Data Ingestion API ----> MongoDB Atlas
        |
        |---- ML Prediction API ----> Saved ML Model
        |
        |---- Document Search API ----> Local RAG Vector Store
        |
        |---- Agent Interaction API ----> Multi-Agent System + MCP Trace
        |
        |---- Azure Sync API ----> Azure Blob Storage
        |
        |---- Azure Search Query API ----> Azure AI Search
        |
        |---- Azure OpenAI Chat API ----> Azure AI Foundry / GPT-4.1
```

## Azure Endpoints

| Endpoint | Purpose |
|---|---|
| `GET /azure-status` | Checks Azure configuration status |
| `POST /azure-sync` | Uploads files to Azure Blob Storage and indexes documents in Azure AI Search |
| `POST /azure-search-query` | Searches project knowledge using Azure AI Search |
| `POST /azure-openai-chat` | Generates GenAI response using Azure GPT-4.1 |

## Security Considerations

This project follows basic security practices for handling cloud credentials.

### Environment Variables

Sensitive values are stored in environment variables instead of being hardcoded in Python files.

Local development uses a `.env` file.

Important variables:

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
AZURE_OPENAI_BASE_URL
AZURE_OPENAI_API_KEY
AZURE_OPENAI_DEPLOYMENT
```

### No Hardcoded Secrets

API keys, MongoDB URI, Azure Storage keys, Azure Search keys, and Azure OpenAI keys are not written directly in the Python source code.

### Azure Web App App Settings

When deployed on Azure Web App, all secrets should be added in:

```text
Azure Web App -> Settings -> Environment Variables -> App Settings
```

The `.env` file should not be pushed to GitHub.

### Git Ignore Protection

The `.gitignore` file should include:

```text
.env
venv/
__pycache__/
.pytest_cache/
*.pyc
```

### Azure Key Vault Recommendation

For production deployment, Azure Key Vault should be used to securely store and manage:

- Azure OpenAI API key
- Azure Storage key
- Azure AI Search admin key
- MongoDB URI

Azure Web App can access Key Vault securely using Managed Identity.

## Module D Verification

- Azure Blob Storage upload completed successfully.
- Azure AI Search index created successfully.
- Azure AI Search query returned relevant matches.
- Azure OpenAI GPT-4.1 generated response successfully.
- Azure configuration is checked using `GET /azure-status`.

---

# Module E: Data Engineering Pipeline

Module E implements a complete data engineering pipeline using Azure Data Factory and Azure SQL Database.

## Tools Used

- Azure Data Factory for ingestion and orchestration
- Azure SQL Database for T-SQL based curated analysis
- Azure Blob Storage for Raw, Staged, and Curated layers
- Parquet format for curated output storage

## Data Engineering Pipeline Diagram

```text
Raw Layer (Azure Blob)
data-engineering/raw/Sample - Superstore.csv
          |
          v
ADF Activity: copy_raw_to_staged
          |
          v
Staged Layer (Azure Blob)
data-engineering/staged/adf_staged_superstore.csv
          |
          v
ADF Activity: copy_staged_to_sql
          |
          v
Azure SQL Table
dbo.superstore_staged_raw
          |
          v
T-SQL Curated Summaries
dbo.curated_region_summary
dbo.curated_category_summary
dbo.curated_monthly_summary
          |
          v
ADF Activity: copy_sql_to_curated_parquet
          |
          v
Curated Parquet Output
data-engineering/curated/curated_region_summary.parquet
```

## Pipeline Flow

Raw Layer:

```text
data-engineering/raw/Sample - Superstore.csv
```

Staged Layer:

```text
data-engineering/staged/adf_staged_superstore.csv
```

SQL Layer:

```text
dbo.superstore_staged_raw
```

Curated SQL Tables:

```text
dbo.curated_region_summary
dbo.curated_category_summary
dbo.curated_monthly_summary
```

Curated Parquet Output:

```text
data-engineering/curated/curated_region_summary.parquet
```

## Azure Data Factory Activities

1. **copy_raw_to_staged**  
   Copies the raw Superstore CSV file into the staged layer.

2. **copy_staged_to_sql**  
   Loads the Superstore dataset into Azure SQL Database.

3. **copy_sql_to_curated_parquet**  
   Exports curated SQL summary data into Parquet format in Azure Blob Storage.

## SQL Usage

T-SQL is used in Azure SQL Database to create curated business summary tables for:

- region-wise sales and profit
- category-wise sales and profit
- monthly sales and profit

## Local Project Proof

```text
src/data_engineering_pipeline.py
data/staged/staged_superstore_sample.csv
data/curated/curated_region_summary.csv
data/curated/curated_category_summary.csv
data/curated/curated_monthly_summary.csv
data/curated/curated_region_summary.parquet
```

## Module E Verification

- ADF pipeline completed successfully.
- SQL table row count: 9994 rows.
- Curated summary tables were created successfully.
- Curated Parquet file was generated in Azure Blob Storage.
- Local data engineering endpoint works successfully.
- Pytest validates Module E output files.

---

# Module F: Analytics and Visualization

This module uses Power BI to visualize the business and AI outputs of the Smart Retail AI Platform.

## Dashboard Pages

1. **Executive Overview**
   - Total Sales
   - Total Profit
   - Total Quantity
   - Average Discount
   - Profit Margin
   - Region-wise Sales
   - Category-wise Sales
   - Monthly Sales Trend

2. **ML Model Outputs**
   - Average Predicted Sales
   - Average Prediction Error
   - Model Record Count
   - Actual Sales vs Predicted Sales
   - Top 20 Prediction Errors
   - Model prediction details

3. **Anomaly Alerts and Agent Insights**
   - Total Anomalies
   - Normal vs Anomaly Count
   - Anomaly Count by Region
   - Anomaly Count by Category
   - Monthly Anomaly Trend
   - AI Agent-Driven Insights
   - Agent Insight Count

## Power BI Data Files

The following dashboard-ready files are generated using:

```text
src/powerbi_data_builder.py
```

Files generated:

```text
powerbi/dashboard_kpis.csv
powerbi/model_outputs.csv
powerbi/anomaly_alerts.csv
powerbi/agent_insights.csv
```

## Power BI Report

```text
powerbi/smart_retail_dashboard.pbix
```

## DAX Measures

Power BI DAX measures are used for KPI and analytical calculations such as:

- total sales
- total profit
- profit margin
- model record count
- average prediction error
- total anomaly alerts
- anomaly rate
- agent insight count

## Module F Verification

- Power BI dashboard file created successfully.
- Dashboard-ready CSV files generated successfully.
- Three dashboard pages created.
- DAX measures added for KPI and analysis.
- Anomaly trends and agent insights are visualized.
- Report is ready for publish/share attempt.

---

# Testing

Run tests:

```powershell
$env:PYTHONPATH = "C:\Users\Hp2\Desktop\smart_retail_project"
python -m pytest tests\test_api.py -v
```

Expected result:

```text
5 passed
```

Test coverage includes:

- data ingestion API
- ML prediction API
- document search API
- agent interaction API
- data engineering pipeline API

---

# How to Run the Project Locally

## 1. Activate virtual environment

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\venv\Scripts\Activate.ps1
```

## 2. Install requirements

```powershell
pip install -r requirements.txt
```

## 3. Run FastAPI server

```powershell
python -m uvicorn api.app:app --reload
```

## 4. Open Swagger UI

```text
http://127.0.0.1:8000/docs
```

---

# Final Verification Checklist

- FastAPI server runs successfully.
- Swagger UI opens successfully.
- All major APIs return successful responses.
- Pytest shows `5 passed`.
- Azure Blob Storage upload is working.
- Azure AI Search query is working.
- Azure OpenAI chat endpoint is working.
- Azure Data Factory pipeline is successful.
- Azure SQL contains 9994 records.
- Curated Parquet output exists.
- Power BI dashboard file exists.
- README documentation is updated.

---

# Known Pending Items

The following items are pending for final live/cloud submission:

1. Azure Web App deployment of the FastAPI backend.
2. Power BI publish/share final confirmation.
3. Final demo video and reflection note.

---

# Project Summary

This project demonstrates an end-to-end Smart Retail AI Platform integrating:

- FastAPI backend
- MongoDB
- ML prediction
- anomaly detection
- RAG document search
- multi-agent AI interaction
- Azure Blob Storage
- Azure AI Search
- Azure OpenAI / Azure AI Foundry
- Azure Data Factory
- Azure SQL Database
- Parquet-based curated data
- Power BI dashboard with DAX measures

---

## Module F Publish Proof

The Power BI dashboard was successfully published to Power BI Service.

Proof screenshots are stored in the dashboard folder:

- dashboard/executive_overview.png
- dashboard/ml_model_outputs.png
- dashboard/anomaly_agent_insights.png
- dashboard/powerbi_publish_success.png
- dashboard/powerbi_service_report.png
- dashboard/powerbi_share_link_sent.png

The final Power BI report file is stored at:

powerbi/smart_retail_dashboard.pbix

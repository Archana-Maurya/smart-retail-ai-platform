from fastapi.testclient import TestClient

from api.app import app

client = TestClient(app)


def test_data_ingestion_api():
    response = client.post("/data-ingestion")
    assert response.status_code == 200
    assert "status" in response.json()


def test_ml_prediction_api():
    payload = {
        "Quantity": 3,
        "Discount": 0.0,
        "Profit": 120.50
    }

    response = client.post("/ml-prediction", json=payload)

    assert response.status_code == 200
    assert "status" in response.json()


def test_document_search_api():
    payload = {
        "question": "What is the ML model used in this project?"
    }

    response = client.post("/document-search", json=payload)

    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert "results" in response.json()


def test_agent_interaction_api():
    payload = {
        "question": "Explain model performance"
    }

    response = client.post("/agent-interaction", json=payload)

    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert "selected_agent" in response.json()
    assert "mcp_trace" in response.json()

def test_data_engineering_pipeline_api():
    response = client.post("/data-engineering-pipeline")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "success"
    assert data["pipeline_flow"] == "Raw -> Staged -> Curated"

    assert data["file_status"]["staged_sample_exists"] == True
    assert data["file_status"]["region_summary_exists"] == True
    assert data["file_status"]["category_summary_exists"] == True
    assert data["file_status"]["monthly_summary_exists"] == True
    assert data["file_status"]["parquet_file_exists"] == True

    assert data["row_counts"]["staged_sample_rows"] == 100
    assert data["row_counts"]["region_summary_rows"] == 4
    assert data["row_counts"]["category_summary_rows"] == 3
    assert data["row_counts"]["monthly_summary_rows"] == 48

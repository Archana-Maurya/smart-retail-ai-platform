from pathlib import Path

import pandas as pd
from fastapi import APIRouter

from src.data_engineering_pipeline import main as run_data_engineering_pipeline

router = APIRouter()


@router.post("/data-engineering-pipeline", summary="Data Engineering Pipeline")
def data_engineering_pipeline():
    try:
        run_data_engineering_pipeline()

        base_dir = Path(__file__).resolve().parent.parent.parent

        staged_file = base_dir / "data" / "staged" / "staged_superstore_sample.csv"
        region_file = base_dir / "data" / "curated" / "curated_region_summary.csv"
        category_file = base_dir / "data" / "curated" / "curated_category_summary.csv"
        monthly_file = base_dir / "data" / "curated" / "curated_monthly_summary.csv"
        parquet_file = base_dir / "data" / "curated" / "curated_region_summary.parquet"

        staged_rows = len(pd.read_csv(staged_file)) if staged_file.exists() else 0
        region_rows = len(pd.read_csv(region_file)) if region_file.exists() else 0
        category_rows = len(pd.read_csv(category_file)) if category_file.exists() else 0
        monthly_rows = len(pd.read_csv(monthly_file)) if monthly_file.exists() else 0

        return {
            "status": "success",
            "message": "Module E data engineering pipeline completed successfully.",
            "pipeline_flow": "Raw -> Staged -> Curated",
            "tools_used": [
                "Azure Data Factory",
                "Azure SQL Database / T-SQL",
                "Parquet-based storage"
            ],
            "file_status": {
                "staged_sample_exists": staged_file.exists(),
                "region_summary_exists": region_file.exists(),
                "category_summary_exists": category_file.exists(),
                "monthly_summary_exists": monthly_file.exists(),
                "parquet_file_exists": parquet_file.exists()
            },
            "row_counts": {
                "staged_sample_rows": staged_rows,
                "region_summary_rows": region_rows,
                "category_summary_rows": category_rows,
                "monthly_summary_rows": monthly_rows
            },
            "azure_pipeline_summary": {
                "raw_layer": "data-engineering/raw/Sample - Superstore.csv",
                "staged_layer": "data-engineering/staged/adf_staged_superstore.csv",
                "sql_table": "dbo.superstore_staged_raw",
                "curated_sql_tables": [
                    "dbo.curated_region_summary",
                    "dbo.curated_category_summary",
                    "dbo.curated_monthly_summary"
                ],
                "curated_parquet": "data-engineering/curated/curated_region_summary.parquet"
            }
        }

    except Exception as error:
        return {
            "status": "failed",
            "message": str(error)
        }

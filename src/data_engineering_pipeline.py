from pathlib import Path
import pandas as pd

# =========================
# Module E: Data Engineering Pipeline
# Raw -> Staged -> Curated
# =========================

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_FILE = BASE_DIR / "data" / "raw" / "Sample - Superstore.csv"

STAGED_DIR = BASE_DIR / "data" / "staged"
CURATED_DIR = BASE_DIR / "data" / "curated"

STAGED_DIR.mkdir(parents=True, exist_ok=True)
CURATED_DIR.mkdir(parents=True, exist_ok=True)

STAGED_SAMPLE_FILE = STAGED_DIR / "staged_superstore_sample.csv"

REGION_SUMMARY_CSV = CURATED_DIR / "curated_region_summary.csv"
CATEGORY_SUMMARY_CSV = CURATED_DIR / "curated_category_summary.csv"
MONTHLY_SUMMARY_CSV = CURATED_DIR / "curated_monthly_summary.csv"
REGION_SUMMARY_PARQUET = CURATED_DIR / "curated_region_summary.parquet"


def load_raw_data():
    print("Reading raw Superstore dataset...")
    return pd.read_csv(RAW_FILE, encoding="latin1")


def clean_data(df):
    print("Cleaning data for staged layer...")

    df = df.copy()

    df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
    df["Ship Date"] = pd.to_datetime(df["Ship Date"], errors="coerce")

    df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce").fillna(0)
    df["Profit"] = pd.to_numeric(df["Profit"], errors="coerce").fillna(0)
    df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce").fillna(0)

    df["Year"] = df["Order Date"].dt.year
    df["Month"] = df["Order Date"].dt.month

    return df


def create_curated_outputs(df):
    print("Creating curated summary outputs...")

    region_summary = df.groupby("Region", as_index=False).agg({
        "Sales": "sum",
        "Profit": "sum",
        "Quantity": "sum"
    })

    category_summary = df.groupby("Category", as_index=False).agg({
        "Sales": "sum",
        "Profit": "sum",
        "Quantity": "sum"
    })

    monthly_summary = df.groupby(["Year", "Month"], as_index=False).agg({
        "Sales": "sum",
        "Profit": "sum"
    })

    region_summary.to_csv(REGION_SUMMARY_CSV, index=False)
    category_summary.to_csv(CATEGORY_SUMMARY_CSV, index=False)
    monthly_summary.to_csv(MONTHLY_SUMMARY_CSV, index=False)

    region_summary.to_parquet(REGION_SUMMARY_PARQUET, index=False)

    return region_summary, category_summary, monthly_summary


def main():
    df = load_raw_data()
    cleaned_df = clean_data(df)

    # Only sample staged file is saved locally to avoid unnecessary large duplicate files
    cleaned_df.head(100).to_csv(STAGED_SAMPLE_FILE, index=False)

    region_summary, category_summary, monthly_summary = create_curated_outputs(cleaned_df)

    print("\n===== MODULE E LOCAL PIPELINE COMPLETED =====")
    print("Total raw records:", len(df))
    print("Staged sample file:", STAGED_SAMPLE_FILE)
    print("Region summary CSV:", REGION_SUMMARY_CSV)
    print("Category summary CSV:", CATEGORY_SUMMARY_CSV)
    print("Monthly summary CSV:", MONTHLY_SUMMARY_CSV)
    print("Curated Parquet file:", REGION_SUMMARY_PARQUET)
    print("Region summary rows:", len(region_summary))
    print("Category summary rows:", len(category_summary))
    print("Monthly summary rows:", len(monthly_summary))


if __name__ == "__main__":
    main()

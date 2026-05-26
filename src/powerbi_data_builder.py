from pathlib import Path

import joblib
import pandas as pd

# =========================
# Module F: Power BI Data Builder
# =========================

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DATA_FILE = BASE_DIR / "data" / "raw" / "Sample - Superstore.csv"
PROCESSED_DATA_FILE = BASE_DIR / "data" / "processed" / "cleaned_superstore.csv"
MODEL_FILE = BASE_DIR / "models" / "superstore_pipeline_model.pkl"
ANOMALY_FILE = BASE_DIR / "data" / "processed" / "anomaly_detected_superstore.csv"

POWERBI_DIR = BASE_DIR / "powerbi"
POWERBI_DIR.mkdir(parents=True, exist_ok=True)

KPI_FILE = POWERBI_DIR / "dashboard_kpis.csv"
MODEL_OUTPUT_FILE = POWERBI_DIR / "model_outputs.csv"
ANOMALY_ALERT_FILE = POWERBI_DIR / "anomaly_alerts.csv"
AGENT_INSIGHTS_FILE = POWERBI_DIR / "agent_insights.csv"


def find_column(df, possible_names):
    normalized_columns = {
        str(col).strip().lower().replace(" ", "_").replace("-", "_"): col
        for col in df.columns
    }

    for name in possible_names:
        key = name.strip().lower().replace(" ", "_").replace("-", "_")
        if key in normalized_columns:
            return normalized_columns[key]

    return None


def load_dataset():
    print("Loading Superstore datasets...")

    processed_df = pd.read_csv(PROCESSED_DATA_FILE, encoding="latin1")

    if RAW_DATA_FILE.exists():
        raw_df = pd.read_csv(RAW_DATA_FILE, encoding="latin1")
    else:
        raw_df = processed_df.copy()

    return processed_df, raw_df


def prepare_label_data(processed_df, raw_df):
    print("Preparing text labels for Power BI...")

    label_source = raw_df if len(raw_df) == len(processed_df) else processed_df

    order_date_col = find_column(label_source, ["Order Date", "Order_Date", "order_date"])
    region_col = find_column(label_source, ["Region", "region"])
    category_col = find_column(label_source, ["Category", "category"])

    labels = pd.DataFrame()

    if region_col:
        labels["Region"] = label_source[region_col]
    else:
        labels["Region"] = "Unknown"

    if category_col:
        labels["Category"] = label_source[category_col]
    else:
        labels["Category"] = "Unknown"

    if order_date_col:
        dates = pd.to_datetime(label_source[order_date_col], errors="coerce")
        labels["Year"] = dates.dt.year
        labels["Month"] = dates.dt.month
        labels["YearMonth"] = dates.dt.strftime("%Y-%m")
    else:
        labels["Year"] = "Unknown"
        labels["Month"] = "Unknown"
        labels["YearMonth"] = "Unknown"

    return labels


def get_numeric_series(df, names, default_value=0):
    col = find_column(df, names)

    if col:
        return pd.to_numeric(df[col], errors="coerce").fillna(default_value)

    return pd.Series([default_value] * len(df))


def build_model_outputs(processed_df, labels):
    print("Creating model output data...")

    model = joblib.load(MODEL_FILE)

    quantity = get_numeric_series(processed_df, ["Quantity", "quantity"])
    discount = get_numeric_series(processed_df, ["Discount", "discount"])
    profit = get_numeric_series(processed_df, ["Profit", "profit"])
    sales = get_numeric_series(processed_df, ["Sales", "sales"])

    # Model was trained using these feature names
    X = pd.DataFrame({
        "Quantity": quantity,
        "Discount": discount,
        "Profit": profit
    })

    predictions = model.predict(X)

    model_df = pd.DataFrame()
    model_df["RecordID"] = range(1, len(processed_df) + 1)
    model_df["Quantity"] = quantity
    model_df["Discount"] = discount
    model_df["Profit"] = profit
    model_df["ActualSales"] = sales
    model_df["PredictedSales"] = predictions
    model_df["PredictionError"] = abs(model_df["ActualSales"] - model_df["PredictedSales"])

    model_df["ErrorCategory"] = model_df["PredictionError"].apply(
        lambda value: "High Error" if value > 500 else "Normal Error"
    )

    model_df["Region"] = labels["Region"]
    model_df["Category"] = labels["Category"]
    model_df["YearMonth"] = labels["YearMonth"]

    model_df.to_csv(MODEL_OUTPUT_FILE, index=False)

    return model_df


def build_anomaly_alerts(processed_df, labels):
    print("Creating anomaly alert data...")

    anomaly_alerts = pd.DataFrame()

    anomaly_alerts["Sales"] = get_numeric_series(processed_df, ["Sales", "sales"])
    anomaly_alerts["Quantity"] = get_numeric_series(processed_df, ["Quantity", "quantity"])
    anomaly_alerts["Discount"] = get_numeric_series(processed_df, ["Discount", "discount"])
    anomaly_alerts["Profit"] = get_numeric_series(processed_df, ["Profit", "profit"])

    # Text values for clean Power BI slicers/charts
    anomaly_alerts["Region"] = labels["Region"]
    anomaly_alerts["Category"] = labels["Category"]
    anomaly_alerts["Year"] = labels["Year"]
    anomaly_alerts["Month"] = labels["Month"]
    anomaly_alerts["YearMonth"] = labels["YearMonth"]

    if ANOMALY_FILE.exists():
        anomaly_df = pd.read_csv(ANOMALY_FILE, encoding="latin1")

        anomaly_col = find_column(
            anomaly_df,
            ["Anomaly", "anomaly", "Anomaly_Status", "Anomaly_Flag", "is_anomaly"]
        )

        if anomaly_col:
            anomaly_values = anomaly_df[anomaly_col].reset_index(drop=True)
        else:
            anomaly_values = pd.Series(["Normal"] * len(processed_df))
    else:
        anomaly_values = pd.Series(["Normal"] * len(processed_df))

    if len(anomaly_values) != len(processed_df):
        anomaly_values = pd.Series(["Normal"] * len(processed_df))

    anomaly_alerts["Anomaly"] = anomaly_values

    anomaly_alerts["Anomaly"] = anomaly_alerts["Anomaly"].replace({
        -1: "Anomaly",
        1: "Normal",
        "1": "Normal",
        "-1": "Anomaly",
        0: "Normal",
        "0": "Normal"
    })

    anomaly_alerts["AlertLevel"] = anomaly_alerts["Anomaly"].apply(
        lambda value: "High Alert" if value == "Anomaly" else "Normal"
    )

    anomaly_alerts.to_csv(ANOMALY_ALERT_FILE, index=False)

    return anomaly_alerts


def build_kpis(processed_df, model_df, anomaly_alerts):
    print("Creating KPI data...")

    total_anomalies = int((anomaly_alerts["Anomaly"] == "Anomaly").sum())

    sales = get_numeric_series(processed_df, ["Sales", "sales"])
    profit = get_numeric_series(processed_df, ["Profit", "profit"])
    quantity = get_numeric_series(processed_df, ["Quantity", "quantity"])
    discount = get_numeric_series(processed_df, ["Discount", "discount"])

    kpi_df = pd.DataFrame({
        "TotalSales": [round(sales.sum(), 2)],
        "TotalProfit": [round(profit.sum(), 2)],
        "TotalQuantity": [int(quantity.sum())],
        "AverageDiscount": [round(discount.mean(), 4)],
        "TotalRecords": [len(processed_df)],
        "TotalAnomalies": [total_anomalies],
        "AveragePredictedSales": [round(model_df["PredictedSales"].mean(), 2)],
        "AveragePredictionError": [round(model_df["PredictionError"].mean(), 2)]
    })

    kpi_df.to_csv(KPI_FILE, index=False)

    return kpi_df


def build_agent_insights():
    print("Creating agent insight data...")

    insights = [
        {
            "AgentName": "Data Analyst Agent",
            "InsightType": "Data Pipeline",
            "Insight": "Superstore data is ingested, cleaned and stored for analytics.",
            "Action": "Use curated data for business reporting."
        },
        {
            "AgentName": "ML Expert Agent",
            "InsightType": "Model Output",
            "Insight": "Sales prediction uses Quantity, Discount and Profit as input features.",
            "Action": "Monitor prediction error and improve model features."
        },
        {
            "AgentName": "ML Expert Agent",
            "InsightType": "Anomaly Detection",
            "Insight": "Isolation Forest detects unusual retail transactions.",
            "Action": "Review high alert records for business risk."
        },
        {
            "AgentName": "Document Assistant Agent",
            "InsightType": "RAG Search",
            "Insight": "RAG vector search retrieves project knowledge and API details.",
            "Action": "Use document search for quick project explanation."
        }
    ]

    insights_df = pd.DataFrame(insights)
    insights_df.to_csv(AGENT_INSIGHTS_FILE, index=False)

    return insights_df


def main():
    processed_df, raw_df = load_dataset()
    labels = prepare_label_data(processed_df, raw_df)

    model_df = build_model_outputs(processed_df, labels)
    anomaly_alerts = build_anomaly_alerts(processed_df, labels)
    kpi_df = build_kpis(processed_df, model_df, anomaly_alerts)
    insights_df = build_agent_insights()

    print("\n===== MODULE F POWER BI DATA READY =====")
    print("KPI file:", KPI_FILE)
    print("Model output file:", MODEL_OUTPUT_FILE)
    print("Anomaly alert file:", ANOMALY_ALERT_FILE)
    print("Agent insights file:", AGENT_INSIGHTS_FILE)
    print("Total records:", len(processed_df))
    print("Model output rows:", len(model_df))
    print("Anomaly alert rows:", len(anomaly_alerts))
    print("Agent insight rows:", len(insights_df))
    print("KPI rows:", len(kpi_df))


if __name__ == "__main__":
    main()

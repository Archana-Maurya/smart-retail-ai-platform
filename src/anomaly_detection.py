import pandas as pd
import joblib

from sklearn.ensemble import IsolationForest

# Load dataset
df = pd.read_csv(
    "../data/processed/preprocessed_superstore.csv"
)

# Features for anomaly detection
X = df[[
    "Sales",
    "Quantity",
    "Discount",
    "Profit"
]]

# Build model
model = IsolationForest(
    n_estimators=100,
    contamination=0.05,
    random_state=42
)

# Train model
model.fit(X)

# Predict anomalies
predictions = model.predict(X)

# Convert output
# -1 = Anomaly
#  1 = Normal

df["Anomaly"] = predictions

df["Anomaly"] = df["Anomaly"].map({
    1: "Normal",
    -1: "Anomaly"
})

# Count anomalies
print("\n===== ANOMALY DETECTION RESULT =====\n")

print(df["Anomaly"].value_counts())

# Show anomaly records
anomalies = df[df["Anomaly"] == "Anomaly"]

print("\n===== ANOMALY RECORDS =====\n")

print(
    anomalies[[
        "Sales",
        "Quantity",
        "Discount",
        "Profit",
        "Anomaly"
    ]].head()
)

# Save anomaly dataset
df.to_csv(
    "../data/processed/anomaly_detected_superstore.csv",
    index=False
)

# Save model
joblib.dump(
    model,
    "../models/anomaly_detection_model.pkl"
)

print("\nAnomaly detection completed!")
print("Model saved successfully!")

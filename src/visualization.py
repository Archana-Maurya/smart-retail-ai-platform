import pandas as pd
import matplotlib.pyplot as plt
import joblib

# =========================
# LOAD MODEL
# =========================

model = joblib.load(
    "../models/superstore_pipeline_model.pkl"
)

print("\nModel Loaded Successfully!")

# =========================
# FEATURE NAMES
# =========================

features = [
    "Quantity",
    "Discount",
    "Profit"
]

# =========================
# FEATURE IMPORTANCE
# =========================

importance = model.feature_importances_

# =========================
# CREATE DATAFRAME
# =========================

importance_df = pd.DataFrame({
    "Feature": features,
    "Importance": importance
})

# =========================
# SORT VALUES
# =========================

importance_df = importance_df.sort_values(
    by="Importance",
    ascending=False
)

print("\nFeature Importance Matrix\n")

print(importance_df)

# =========================
# VISUALIZATION
# =========================

plt.figure(figsize=(8, 5))

plt.bar(
    importance_df["Feature"],
    importance_df["Importance"]
)

plt.xlabel("Features")

plt.ylabel("Importance Score")

plt.title("Feature Importance Visualization")

plt.tight_layout()

plt.show()
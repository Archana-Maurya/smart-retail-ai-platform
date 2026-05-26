import pandas as pd
import joblib

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# Load model
model = joblib.load(
    "../models/superstore_pipeline_model.pkl"
)

# Load dataset
df = pd.read_csv(
    "../data/processed/cleaned_superstore.csv",
    encoding="latin1"
)

# Features
features = [
    "Quantity",
    "Discount",
    "Profit"
]

# Input and target
X = df[features]

y = df["Sales"]

# Predictions
predictions = model.predict(X)

# Metrics
mae = mean_absolute_error(y, predictions)

mse = mean_squared_error(y, predictions)

r2 = r2_score(y, predictions)

# Print results
print("\nMean Absolute Error :", round(mae, 2))

print("Mean Squared Error :", round(mse, 2))

print("R2 Score :", round(r2, 4))
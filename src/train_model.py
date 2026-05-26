import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# Load dataset
df = pd.read_csv(
    "../data/processed/cleaned_superstore.csv",
    encoding="latin1"
)

# Select features
features = [
    "Quantity",
    "Discount",
    "Profit"
]

# Input and target
X = df[features]

y = df["Sales"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

# Train model
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, predictions)

r2 = r2_score(y_test, predictions)

print("\nMean Absolute Error :", round(mae, 2))

print("R2 Score :", round(r2, 4))

# Save model
joblib.dump(
    model,
    "../models/superstore_pipeline_model.pkl"
)

print("\nModel saved successfully!")
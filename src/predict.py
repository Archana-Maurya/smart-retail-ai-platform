import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv(
    "../data/processed/preprocessed_superstore.csv"
)

# Create target column
df["Sales_Category"] = df["Sales"].apply(
    lambda x: 1 if x > 500 else 0
)

# Features
X = df[[
    "Category",
    "Region",
    "Segment",
    "Quantity",
    "Discount",
    "Profit",
    "Year",
    "Month",
    "Day"
]]

# Target
y = df["Sales_Category"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train model
model.fit(X_train, y_train)

# Save model as .pkl file
joblib.dump(
    model,
    "../models/superstore_pipeline_model.pkl"
)

print("Model trained and saved successfully!")
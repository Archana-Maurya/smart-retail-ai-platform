import pandas as pd
import joblib

from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv(
    "../data/processed/feature_engineered_superstore.csv"
)

# Categorical columns
categorical_cols = [
    "Category",
    "Region",
    "Segment"
]

# Label encoding
label_encoders = {}

for col in categorical_cols:

    le = LabelEncoder()

    df[col] = le.fit_transform(df[col])

    label_encoders[col] = le

# Save encoders
joblib.dump(
    label_encoders,
    "../models/label_encoders.pkl"
)

# Save processed dataset
df.to_csv(
    "../data/processed/preprocessed_superstore.csv",
    index=False
)

print("Preprocessing completed!")
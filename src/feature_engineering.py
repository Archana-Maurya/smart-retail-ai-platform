import pandas as pd

# Load dataset
df = pd.read_csv(
    "../data/processed/cleaned_superstore.csv"
)

# Convert date
df["Order Date"] = pd.to_datetime(
    df["Order Date"]
)

# Extract features
df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month
df["Day"] = df["Order Date"].dt.day

# Save dataset
df.to_csv(
    "../data/processed/feature_engineered_superstore.csv",
    index=False
)

print("Feature engineering completed!")
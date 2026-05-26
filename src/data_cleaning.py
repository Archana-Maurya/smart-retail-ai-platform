import pandas as pd

# Load dataset
df = pd.read_csv(
    "../data/raw/Sample - Superstore.csv",
    encoding="latin1"
)

# Missing values
print(df.isnull().sum())


# Fill missing values
df.fillna(0, inplace=True)

# Convert dates
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

# Save dataset
df.to_csv(
    "../data/processed/cleaned_superstore.csv",
    index=False
)

print("Data cleaning completed!")
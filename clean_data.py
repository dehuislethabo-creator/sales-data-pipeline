import pandas as pd

# Load the raw Kaggle sales dataset
df = pd.read_csv("sales_data_sample.csv")

# Standardise column names: lowercase and underscores
df.columns = df.columns.str.strip().str.lower()

# Remove duplicate rows
df = df.drop_duplicates()

# Remove rows missing essential values
df = df.dropna(subset=["productline", "quantityordered", "priceeach", "orderdate"])

# Convert order date to datetime
df["orderdate"] = pd.to_datetime(df["orderdate"], errors="coerce")

# Remove invalid quantities or prices
df = df[df["quantityordered"] > 0]
df = df[df["priceeach"] > 0]

# Save cleaned data
df.to_csv("cleaned_sales_data.csv", index=False)

print("Data cleaned successfully.")
print(df.head())

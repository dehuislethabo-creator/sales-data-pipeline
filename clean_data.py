import pandas as pd

# Load the raw sales data
df = pd.read_csv("sales_data.csv")

# Remove duplicate rows
df = df.drop_duplicates()

# Remove rows with missing essential values
df = df.dropna(subset=["product", "quantity", "price"])

# Convert date column to datetime format
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

# Remove invalid prices or quantities
df = df[df["price"] > 0]
df = df[df["quantity"] > 0]

# Save the cleaned data
df.to_csv("cleaned_sales_data.csv", index=False)

print("Data cleaned successfully.")
print(df.head())

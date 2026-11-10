# Sales Data Pipeline

A beginner data-engineering project that cleans a public Kaggle sales dataset and prepares it for SQL analysis.

## Objective

To practise the basic data-engineering workflow:

1. Load raw data
2. Clean and validate it
3. Prepare it for analysis
4. Query it using SQL
5. Document the process

## Dataset

The project uses the public **Sample Sales Data** dataset from Kaggle.

It contains sales-order information, including order number, quantity ordered, unit price, sales amount, order date, product line, customer name and order status.

## Tools

- Python
- Pandas
- SQL
- Git
- GitHub

## Pipeline

1. Load the raw Kaggle sales CSV.
2. Standardise column names.
3. Remove duplicate rows.
4. Remove rows with missing essential values.
5. Convert order dates to datetime format.
6. Remove invalid quantities and prices.
7. Save the cleaned dataset as `cleaned_sales_data.csv`.
8. Use SQL to analyse sales by product, month, customer and order status.

## Business Questions

- Which product lines generate the most sales?
- Which months have the highest sales?
- Which customers spend the most?
- How do order statuses affect sales?

## How to Run

1. Install Python.
2. Install the required packages:

```bash
pip install -r requirements.txt



-- Total sales by product line
SELECT
    productline,
    SUM(sales) AS total_sales
FROM sales_data
GROUP BY productline
ORDER BY total_sales DESC;

-- Monthly sales revenue
SELECT
    strftime('%Y-%m', orderdate) AS sales_month,
    SUM(sales) AS total_sales
FROM sales_data
GROUP BY sales_month
ORDER BY sales_month;

-- Top customers by sales
SELECT
    customername,
    SUM(sales) AS total_sales
FROM sales_data
GROUP BY customername
ORDER BY total_sales DESC
LIMIT 10;

-- Sales by order status
SELECT
    status,
    SUM(sales) AS total_sales
FROM sales_data
GROUP BY status
ORDER BY total_sales DESC;

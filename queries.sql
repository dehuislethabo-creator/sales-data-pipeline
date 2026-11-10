-- Total revenue by product
SELECT
    product,
    SUM(quantity * price) AS total_revenue
FROM sales_data
GROUP BY product
ORDER BY total_revenue DESC;

-- Monthly sales revenue
SELECT
    strftime('%Y-%m', order_date) AS sales_month,
    SUM(quantity * price) AS total_revenue
FROM sales_data
GROUP BY sales_month
ORDER BY sales_month;

-- Top customers by spend
SELECT
    customer_name,
    SUM(quantity * price) AS total_spent
FROM sales_data
GROUP BY customer_name
ORDER BY total_spent DESC
LIMIT 10;

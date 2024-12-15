SELECT customer_id, AVG(amount) AS average_sales
FROM sales
GROUP BY customer_id
ORDER BY average_sales DESC;

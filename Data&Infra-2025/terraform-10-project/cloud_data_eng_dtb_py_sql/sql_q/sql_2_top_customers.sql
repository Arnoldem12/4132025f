SELECT customer_name, SUM(amount) AS total
FROM customer_orders
GROUP BY customer_name
ORDER BY total DESC
LIMIT 5;
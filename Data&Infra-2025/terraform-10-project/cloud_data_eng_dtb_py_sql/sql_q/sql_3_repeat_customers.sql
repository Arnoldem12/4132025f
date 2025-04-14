SELECT customer_name
FROM customer_orders
GROUP BY customer_name
HAVING COUNT(*) > 1;
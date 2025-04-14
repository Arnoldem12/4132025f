SELECT DATE_FORMAT(order_date, '%Y-%m') AS month, SUM(amount) AS monthly_total
FROM customer_orders
GROUP BY month
ORDER BY month;
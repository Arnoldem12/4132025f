SELECT 
  customer_name,
  SUM(amount) AS total_spent,
  MAX(order_date) AS last_order
FROM customer_orders
GROUP BY customer_name;
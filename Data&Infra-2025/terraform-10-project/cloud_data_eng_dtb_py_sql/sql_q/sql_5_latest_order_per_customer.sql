SELECT *
FROM customer_orders co
WHERE order_date = (
  SELECT MAX(order_date)
  FROM customer_orders
  WHERE customer_name = co.customer_name
);
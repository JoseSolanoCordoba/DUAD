-- SQLite
SELECT product_id, sum(total_amount)
FROM Products_per_Invoice
GROUP BY product_id;
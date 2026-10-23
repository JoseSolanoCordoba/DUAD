-- SQLite
UPDATE Products
SET stock_available = 0
WHERE price <= 0;
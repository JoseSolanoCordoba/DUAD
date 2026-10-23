-- SQLite
UPDATE Products
SET price = price + 100
WHERE stock_available < 10;
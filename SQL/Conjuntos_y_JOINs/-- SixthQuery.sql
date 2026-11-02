-- SQLite
SELECT Customers.id, Customers.name
FROM Customers
LEFT JOIN Rents 
ON Customers.id = Rents.customer_id
WHERE Rents.customer_id IS NULL
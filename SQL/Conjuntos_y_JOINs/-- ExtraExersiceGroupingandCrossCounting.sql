-- SQLite
SELECT Customers.id, Customers.name AS customer_name, COUNT(Rents.customer_id) AS count
FROM Rents
INNER JOIN Customers
ON Customers.id = Rents.customer_id
GROUP BY Customers.id
ORDER BY count DESC
LIMIT 3
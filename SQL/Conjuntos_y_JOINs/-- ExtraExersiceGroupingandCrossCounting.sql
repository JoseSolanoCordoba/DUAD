-- SQLite
SELECT Customers.id, Customers.name as customer_name, Books.name as book_name,COUNT(Rents.customer_id) as count
FROM Rents
INNER JOIN Customers
ON Customers.id = Rents.customer_id
INNER JOIN Books
ON Books.id = Rents.book_id
GROUP BY Books.id, Customers.id
ORDER BY count DESC
LIMIT 3
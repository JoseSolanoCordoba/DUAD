-- SQLite
SELECT Customers.name AS customer_name, Books.name AS book_name, Authors.name AS author_name, Rents.state AS state
FROM Rents
INNER JOIN Customers
ON Customers.id = Rents.customer_id
INNER JOIN Books
ON Books.id = Rents.book_id
LEFT JOIN Authors
ON Authors.id = Books.author_id
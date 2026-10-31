-- SQLite
SELECT Books.id, Books.name
FROM Books
LEFT JOIN Rents 
ON Books.id = Rents.book_id
WHERE Rents.state = 'Overdue'
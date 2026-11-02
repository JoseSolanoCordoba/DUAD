-- SQLite
SELECT Books.id, Books.name
FROM Books
LEFT JOIN Rents 
ON Books.id = Rents.book_id
WHERE Rents.book_id IS NULL
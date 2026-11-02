-- SQLite
SELECT DISTINCT Books.id, Books.name
FROM Books
INNER JOIN Rents 
ON Books.id = Rents.book_id

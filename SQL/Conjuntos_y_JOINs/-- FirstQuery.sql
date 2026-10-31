-- SQLite
SELECT Books.name, Authors.name
FROM Books
LEFT JOIN Authors 
ON Books.author_id = Authors.id
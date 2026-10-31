-- SQLite
SELECT Books.name, Authors.name
FROM Books
LEFT JOIN Authors 
ON Books.author_id = Authors.id
WHERE Books.author_id IS NULL
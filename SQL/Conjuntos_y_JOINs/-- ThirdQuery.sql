-- SQLite
SELECT Authors.name
FROM Authors
LEFT JOIN Books 
ON Books.author_id = Authors.id
WHERE Books.author_id IS NULL
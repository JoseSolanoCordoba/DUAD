-- SQLite
INSERT INTO Books (id, name, author_id)
VALUES (1, 'Don Quijote', 1);

INSERT INTO Books (id, name, author_id)
VALUES (2, 'La Divina Comedia', 2);

INSERT INTO Books (id, name, author_id)
VALUES (3, 'Vagabond 1-3', 3);

INSERT INTO Books (id, name, author_id)
VALUES (4, 'Dragon Ball 1', 4);

INSERT INTO Books (id, name, author_id)
VALUES (5, 'The Book of the 5 Rings', NULL);


INSERT INTO Authors (id, name)
VALUES (1, 'Miguel de Cervantes');

INSERT INTO Authors (id, name)
VALUES (2, 'Dante Alighieri');

INSERT INTO Authors (id, name)
VALUES (3, 'Takehiko Inoue');

INSERT INTO Authors (id, name)
VALUES (4, 'Akira Toriyama');

INSERT INTO Authors (id, name)
VALUES (5, 'Walt Disney');


INSERT INTO Customers (id, name, email)
VALUES (1, 'John Doe', 'j.doe@email.com');

INSERT INTO Customers (id, name, email)
VALUES (2, 'Jane Doe', 'jane@doe.com');

INSERT INTO Customers (id, name, email)
VALUES (3, 'Luke Skywalker', 'darth.son@email.com');


INSERT INTO Rents (id, book_id, customer_id, state)
VALUES (1, 1, 2, 'Returned');

INSERT INTO Rents (id, book_id, customer_id, state)
VALUES (2, 2, 2, 'Returned');

INSERT INTO Rents (id, book_id, customer_id, state)
VALUES (3, 1, 1, 'On time');

INSERT INTO Rents (id, book_id, customer_id, state)
VALUES (4, 3, 1, 'On time');

INSERT INTO Rents (id, book_id, customer_id, state)
VALUES (5, 2, 2, 'Overdue');
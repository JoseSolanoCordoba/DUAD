-- SQLite
CREATE TABLE Invoices(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER REFERENCES Users(id),
    purchase_date TIMESTAMP NOT NULL,
    total_amount DECIMAL(8, 2) NOT NULL,
    method_id REFERENCES Payment_Methods(id)
);
CREATE TABLE Products_per_Invoice(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    invoice_id INTEGER REFERENCES Invoices(id),
    product_id INTEGER REFERENCES Products(id),
    total_amount DECIMAL(8, 2) NOT NULL,
    quantity INTEGER NOT NULL
);

CREATE TABLE Products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(10) NOT NULL,
    price DECIMAL(8, 2) NOT NULL,
    entry_date TIMESTAMP NOT NULL,
    brand VARCHAR(10) NOT NULL,
    stock_available INTEGER DEFAULT 0
);
CREATE TABLE Shopping_Cart_Products(
    buyer_email VARCHAR(25) NOT NULL,
    product_id INTEGER REFERENCES Products(id),
    quantity INTEGER NOT NULL
);
CREATE TABLE Users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name VARCHAR(25) NOT NULL,
    email VARCHAR(25) NOT NULL,
    registration_date TIMESTAMP NOT NULL
);
CREATE TABLE Reviews(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER REFERENCES Users(id),
    product_id INTEGER REFERENCES Products(id),
    comment TEXT NOT NULL,
    rating SMALLINTEGER NOT NULL,
    date DATE NOT NULL
);
CREATE TABLE Payment_Methods(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    method_type VARCHAR(10) NOT NULL,
    bank_name VARCHAR(15) NOT NULL
);

-- SQLite
ALTER TABLE Invoices
ADD COLUMN phone_number VARCHAR(15) CHECK (length(phone_number) <= 15) ;

ALTER TABLE Invoices
ADD COLUMN employee_id INTEGER;

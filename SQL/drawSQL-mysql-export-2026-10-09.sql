CREATE TABLE `Invoices`(
    `Invoice Number` BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Purchase date` TIMESTAMP NOT NULL,
    `Buyer email` VARCHAR(255) NOT NULL,
    `Total amount` DECIMAL(8, 2) NOT NULL
);
CREATE TABLE `Products per Invoice`(
    `Quantity` BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Total amount` DECIMAL(8, 2) NOT NULL
);
CREATE TABLE `Shopping Cart`(
    `Buyer email` VARCHAR(255) NOT NULL,
    `Products` BIGINT NOT NULL,
    PRIMARY KEY(`Buyer email`)
);
CREATE TABLE `Products`(
    `Code` BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Name` VARCHAR(255) NOT NULL,
    `Price` DECIMAL(8, 2) NOT NULL,
    `Entry date` TIMESTAMP NOT NULL,
    `Brand` VARCHAR(255) NOT NULL,
    `Stock available` BOOLEAN NOT NULL
);
CREATE TABLE `Quantity per Invoice`(
    `Invoice Number` BIGINT NOT NULL,
    `Quantity` BIGINT NOT NULL
);
ALTER TABLE
    `Quantity per Invoice` ADD UNIQUE `quantity per invoice_invoice number_unique`(`Invoice Number`);
ALTER TABLE
    `Products per Invoice` ADD CONSTRAINT `products per invoice_quantity_foreign` FOREIGN KEY(`Quantity`) REFERENCES `Quantity per Invoice`(`Quantity`);
ALTER TABLE
    `Invoices` ADD CONSTRAINT `invoices_buyer email_foreign` FOREIGN KEY(`Buyer email`) REFERENCES `Shopping Cart`(`Buyer email`);
ALTER TABLE
    `Products` ADD CONSTRAINT `products_code_foreign` FOREIGN KEY(`Code`) REFERENCES `Shopping Cart`(`Products`);
ALTER TABLE
    `Quantity per Invoice` ADD CONSTRAINT `quantity per invoice_invoice number_foreign` FOREIGN KEY(`Invoice Number`) REFERENCES `Invoices`(`Invoice Number`);
CREATE TABLE `Invoices`(
    `Invoice Number` BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Purchase date` TIMESTAMP NOT NULL,
    `Buyer email` VARCHAR(255) NOT NULL,
    `Total amount` DECIMAL(8, 2) NOT NULL
);
CREATE TABLE `Products per Invoice`(
    `Invoice number` BIGINT NOT NULL AUTO_INCREMENT,
    `Product Code` BIGINT NOT NULL,
    `Total amount` DECIMAL(8, 2) NOT NULL,
    `Quantity` BIGINT NOT NULL
);
CREATE TABLE `Shopping Cart`(
    `Buyer email` VARCHAR(255) NOT NULL,
    `Products` BIGINT NOT NULL,
    PRIMARY KEY(`Buyer email`)
);
CREATE TABLE `Products`(
    `Product Code` BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Name` VARCHAR(255) NOT NULL,
    `Price` DECIMAL(8, 2) NOT NULL,
    `Entry date` TIMESTAMP NOT NULL,
    `Brand` VARCHAR(255) NOT NULL,
    `Stock available` INT NOT NULL
);
CREATE TABLE `Shopping Cart Products`(
    `Buyer email` VARCHAR(255) NOT NULL,
    `Product Code` BIGINT NOT NULL,
    `Quantity` BIGINT NOT NULL
);
ALTER TABLE
    `Products` ADD CONSTRAINT `products_product code_foreign` FOREIGN KEY(`Product Code`) REFERENCES `Shopping Cart Products`(`Product Code`);
ALTER TABLE
    `Products` ADD CONSTRAINT `products_product code_foreign` FOREIGN KEY(`Product Code`) REFERENCES `Products per Invoice`(`Product Code`);
ALTER TABLE
    `Invoices` ADD CONSTRAINT `invoices_invoice number_foreign` FOREIGN KEY(`Invoice Number`) REFERENCES `Products per Invoice`(`Invoice number`);
ALTER TABLE
    `Shopping Cart` ADD CONSTRAINT `shopping cart_buyer email_foreign` FOREIGN KEY(`Buyer email`) REFERENCES `Shopping Cart Products`(`Buyer email`);
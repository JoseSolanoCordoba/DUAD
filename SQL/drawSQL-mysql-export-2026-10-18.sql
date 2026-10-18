CREATE TABLE `Invoices`(
    `Invoice Number` BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `User ID` BIGINT NOT NULL,
    `Purchase date` TIMESTAMP NOT NULL,
    `Buyer email` VARCHAR(255) NOT NULL,
    `Total amount` DECIMAL(8, 2) NOT NULL,
    `Method ID` BIGINT NOT NULL
);
CREATE TABLE `Products per Invoice`(
    `Invoice number` BIGINT NOT NULL AUTO_INCREMENT,
    `Product Code` BIGINT NOT NULL,
    `Total amount` DECIMAL(8, 2) NOT NULL,
    `Quantity` BIGINT NOT NULL
);
CREATE TABLE `Shopping Cart`(
    `Buyer email` VARCHAR(255) NOT NULL,
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
CREATE TABLE `Users`(
    `ID` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Full name` VARCHAR(255) NOT NULL,
    `Email` VARCHAR(255) NOT NULL,
    `Registration date` TIMESTAMP NOT NULL
);
ALTER TABLE
    `Users` ADD UNIQUE `users_email_unique`(`Email`);
CREATE TABLE `Reviews`(
    `Review ID` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `User ID` BIGINT NOT NULL,
    `Product Code` BIGINT NOT NULL,
    `Comment` TEXT NOT NULL,
    `Rating` SMALLINT NOT NULL,
    `Date` DATE NOT NULL
);
CREATE TABLE `Payment Methods`(
    `Method ID` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Method type` VARCHAR(255) NOT NULL,
    `Bank name` VARCHAR(255) NOT NULL
);
ALTER TABLE
    `Reviews` ADD CONSTRAINT `reviews_product code_foreign` FOREIGN KEY(`Product Code`) REFERENCES `Products`(`Product Code`);
ALTER TABLE
    `Reviews` ADD CONSTRAINT `reviews_user id_foreign` FOREIGN KEY(`User ID`) REFERENCES `Users`(`ID`);
ALTER TABLE
    `Invoices` ADD CONSTRAINT `invoices_invoice number_foreign` FOREIGN KEY(`Invoice Number`) REFERENCES `Products per Invoice`(`Invoice number`);
ALTER TABLE
    `Invoices` ADD CONSTRAINT `invoices_user id_foreign` FOREIGN KEY(`User ID`) REFERENCES `Users`(`ID`);
ALTER TABLE
    `Products` ADD CONSTRAINT `products_product code_foreign` FOREIGN KEY(`Product Code`) REFERENCES `Shopping Cart Products`(`Product Code`);
ALTER TABLE
    `Shopping Cart` ADD CONSTRAINT `shopping cart_buyer email_foreign` FOREIGN KEY(`Buyer email`) REFERENCES `Shopping Cart Products`(`Buyer email`);
ALTER TABLE
    `Products` ADD CONSTRAINT `products_product code_foreign` FOREIGN KEY(`Product Code`) REFERENCES `Products per Invoice`(`Product Code`);
ALTER TABLE
    `Payment Methods` ADD CONSTRAINT `payment methods_method id_foreign` FOREIGN KEY(`Method ID`) REFERENCES `Invoices`(`Method ID`);
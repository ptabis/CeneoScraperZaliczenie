CREATE DATABASE `ceneo`;

USE `ceneo`;

CREATE TABLE `products` (
    `id` INT PRIMARY KEY NOT NULL,
    `name` VARCHAR(255),
    `subname` VARCHAR(255),
    `price` VARCHAR(100),
    `score` VARCHAR(6)
);

CREATE TABLE `opinions` (
    `id` INT PRIMARY KEY NOT NULL,
    `product_id` INT NOT NULL,
    `author` VARCHAR(125),
    `recommendation` varchar(15),
    `stars` VARCHAR(5),
    `content` TEXT,
    `pros` TEXT,
    `cons` TEXT,
    `useful` INT,
    `useless` INT,
    `purchased` BOOL,
    `review_date` DATETIME,
    `purchase_date` DATETIME,
    FOREIGN KEY (`product_id`)
    REFERENCES `products`(`id`)
);
CREATE DATABASE `ceneo`;

USE `ceneo`;

CREATE TABLE `opinions` (
    `id` INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    `author` VARCHAR(125),
    `recommendation` varchar(15),
    `stars` VARCHAR(3),
    `content` TEXT,
    `pros` TEXT,
    `cons` TEXT,
    `useful` INT,
    `useless` INT,
    `purchased` BOOL,
    `review_date` DATETIME,
    `purchase_date` DATETIME
);
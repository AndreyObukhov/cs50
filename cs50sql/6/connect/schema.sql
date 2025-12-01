-- Deletes prior tables if they exist
DROP TABLE IF EXISTS `users`;
DROP TABLE IF EXISTS `schools`;
DROP TABLE IF EXISTS `companies`;
DROP TABLE IF EXISTS `user_and_user`;
DROP TABLE IF EXISTS `company_and_user`;
DROP TABLE IF EXISTS `school_and_user`;

-- Creates tables with updated schema
CREATE TABLE `users` (
    `id` INT UNSIGNED AUTO_INCREMENT,
    `first_name` VARCHAR(128) NOT NULL,
    `last_name` VARCHAR(128),
    `username` VARCHAR(128) NOT NULL UNIQUE,
    `password` VARCHAR(128) NOT NULL,
    PRIMARY KEY(`id`)
);

CREATE TABLE `schools` (
    `id` INT UNSIGNED AUTO_INCREMENT,
    `name` VARCHAR(128) NOT NULL,
    `type` ENUM('Primary', 'Secondary', 'Higher Education'),
    `location` VARCHAR(128),
    `year` YEAR,
    PRIMARY KEY(`id`)
);

CREATE TABLE `companies` (
    `id` INT UNSIGNED AUTO_INCREMENT,
    `name` VARCHAR(128) NOT NULL,
    `industry` ENUM('Technology', 'Education', 'Business'),
    `location` VARCHAR(128),
    PRIMARY KEY(`id`)
);

CREATE TABLE `user_and_user` (
    `id` INT UNSIGNED AUTO_INCREMENT,
    `user1_id` INT UNSIGNED,
    `user2_id` INT UNSIGNED,
    PRIMARY KEY(`id`),
    FOREIGN KEY(`user1_id`) REFERENCES `users`(`id`),
    FOREIGN KEY(`user2_id`) REFERENCES `users`(`id`)
);

CREATE TABLE `company_and_user` (
    `id` INT UNSIGNED AUTO_INCREMENT,
    `start` DATE,
    `end` DATE,
    `title` VARCHAR(128),
    `user_id` INT UNSIGNED,
    `company_id` INT UNSIGNED,
    PRIMARY KEY(`id`),
    FOREIGN KEY(`user_id`) REFERENCES `users`(`id`),
    FOREIGN KEY(`company_id`) REFERENCES `users`(`id`)
);

CREATE TABLE `school_and_user` (
    `id` INT UNSIGNED AUTO_INCREMENT,
    `start` DATE,
    `graduation` DATE,
    `degree` VARCHAR(16),
    `user_id` INT UNSIGNED,
    `school_id` INT UNSIGNED,
    PRIMARY KEY(`id`),
    FOREIGN KEY(`user_id`) REFERENCES `users`(`id`),
    FOREIGN KEY(`school_id`) REFERENCES `schools`(`id`)
);

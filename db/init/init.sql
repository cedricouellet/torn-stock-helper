-- Represents a stock in Torn City
CREATE TABLE `stock` (
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `torn_id` INT UNSIGNED NOT NULL UNIQUE,
    `name` VARCHAR(100) NOT NULL,
    `acronym` VARCHAR(3) NOT NULL,
    `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP
);

-- Represents the snapshot, or saved state of a stock
CREATE TABLE `snapshot` (
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `stock_id` INT UNSIGNED NOT NULL, 
    `date` DATETIME NOT NULL DEFAULT NOW(),
    `timestamp` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `open_price` DECIMAL(10, 2) NOT NULL,
    `high_price` DECIMAL(10, 2) NOT NULL,
    `low_price` DECIMAL(10, 2) NOT NULL,
    `close_price` DECIMAL(10, 2) NOT NULL,
    `volume` BIGINT(20) NOT NULL,
    `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
    INDEX `date` (`date` ASC),
    INDEX `stock_id` (`stock_id` ASC),
    CONSTRAINT `fk_stock_id`
        FOREIGN KEY (`stock_id`)
        REFERENCES `stock` (`id`)
        ON UPDATE NO ACTION
        ON DELETE CASCADE
        
);

-- Represents a generated prediction for a stock
CREATE TABLE `prediction` (
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `stock_id` INT UNSIGNED NOT NULL,
    `date` DATETIME NOT NULL DEFAULT NOW(),
    `close_price` DECIMAL(10, 2) NOT NULL,
    `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
    INDEX `date` (`date` ASC),
    INDEX `stock_id` (`stock_id` ASC),
        CONSTRAINT `fk_stock_id`
        FOREIGN KEY (`stock_id`)
        REFERENCES `stock` (`id`)
        ON UPDATE NO ACTION
        ON DELETE CASCADE
        
);


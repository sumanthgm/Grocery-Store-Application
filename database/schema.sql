-- Schema reconstructed from the queries in backend/*_dao.py.
CREATE DATABASE IF NOT EXISTS grocery_store;
USE grocery_store;

CREATE TABLE IF NOT EXISTS uom (
    uom_id   INT AUTO_INCREMENT PRIMARY KEY,
    uom_name VARCHAR(45) NOT NULL
);

CREATE TABLE IF NOT EXISTS products (
    product_id     INT AUTO_INCREMENT PRIMARY KEY,
    name           VARCHAR(100) NOT NULL,
    uom_id         INT NOT NULL,
    price_per_unit DOUBLE NOT NULL,
    FOREIGN KEY (uom_id) REFERENCES uom (uom_id)
);

CREATE TABLE IF NOT EXISTS `order` (
    order_id  INT AUTO_INCREMENT PRIMARY KEY,
    customer  VARCHAR(100) NOT NULL,
    total     DOUBLE NOT NULL,
    date_time DATETIME NOT NULL
);

CREATE TABLE IF NOT EXISTS order_details (
    order_id    INT NOT NULL,
    product_id  INT NOT NULL,
    quantity    DOUBLE NOT NULL,
    total_price DOUBLE NOT NULL,
    PRIMARY KEY (order_id, product_id),
    FOREIGN KEY (order_id) REFERENCES `order` (order_id),
    FOREIGN KEY (product_id) REFERENCES products (product_id)
);

INSERT INTO uom (uom_name) VALUES ('each'), ('kg');

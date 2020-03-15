DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS order_set;
CREATE TABLE order_set(
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  start_time DATETIME NOT NULL,
  end_time DATETIME NOT NULL,
  total INTEGER NOT NULL,
  order_max TINYINT DEFAULT 3
);

CREATE TABLE orders(
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  order_id INTEGER NOT NULL,
  phone CHAR(11) NOT NULL,
  name VARCHAR(32) NOT NULL,
  id_number CHAR(18) NOT NULL,
  order_num TINYINT NOT NULL,
  status TINYINT DEFAULT 0,
  create_time DATETIME DEFAULT CURRENT_TIMESTAMP(),
  FOREIGN KEY orders(order_id) REFERENCES order_set(id)
)charset=utf8mb4;
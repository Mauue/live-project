DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS order_set;
DROP TABLE IF EXISTS admin;
CREATE TABLE order_set(
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  start_time DATETIME NOT NULL,
  end_time DATETIME NOT NULL,
  total INTEGER NOT NULL,
  order_max TINYINT DEFAULT 3
);

CREATE TABLE orders(
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  round_id INTEGER NOT NULL,
  phone CHAR(11) NOT NULL,
  name VARCHAR(32) NOT NULL,
  id_number CHAR(18) NOT NULL,
  order_num TINYINT NOT NULL,
  status TINYINT DEFAULT 0,
  create_time DATETIME DEFAULT CURRENT_TIMESTAMP(),
  FOREIGN KEY orders(round_id) REFERENCES order_set(id)
)charset=utf8mb4;

CREATE TABLE IF NOT EXISTS admin(
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  username varchar(32) not null unique ,
  password varchar(200) not null
)charset=utf8mb4;
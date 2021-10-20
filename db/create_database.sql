CREATE TABLE seller (
    id integer not null auto_increment,
    seller_name varchar(200) not null,
    CONSTRAINT PK_seller PRIMARY KEY (id)
);

CREATE TABLE sale (
    id integer not null auto_increment,
    seller_id integer NOT NULL,
    customer_name varchar(200) NOT NULL,
    created_at datetime DEFAULT CURRENT_TIMESTAMP,
    item_name varchar(200) NOT NULL,
    item_value float NOT NULL,
    CONSTRAINT PK_sale PRIMARY KEY (id),
    CONSTRAINT FOREIGN KEY (seller_id) REFERENCES seller(id) ON DELETE CASCADE
);

SET character_set_client = utf8;
SET character_set_connection = utf8;
SET character_set_results = utf8;
SET collation_connection = utf8_general_ci;


INSERT INTO seller (seller_name) VALUES ('seller_1'),('seller_2'),('seller_3'),('seller_4'),('seller_5');
-- CREATE SCHEMA
create schema see_tickets;

-- CREATE TABLE FEE
create table see_tickets.fee (
	id serial primary key,
	value FLOAT not null,
	currency varchar(50)
);

-- CREATE TABLE EVENTS
create table see_tickets.events (
	id serial primary key,
	name varchar(150) not null,
	fee_id INT not null,
	foreign key (fee_id)
		references see_tickets.fee (id)

);

-- CREATE TABE PRODUCTS
create table see_tickets.products (
	id serial primary key,
	name varchar(150) not null,
	fee_id INT not null,
	foreign key (fee_id)
		references see_tickets.fee (id)
);

-- CREATE TABLE EVENT_PRODUCT
create table see_tickets.event_product (
	event_id INT not null,
	product_id INT not null,
	primary key(event_id, product_id),
	foreign key (product_id)
		references see_tickets.products (id),
	foreign key (event_id)
		references see_tickets.events (id)
);


-- INSERTS

-- FEE
INSERT INTO see_tickets.fee (value, currency)
VALUES(10, 'EURO');
INSERT INTO see_tickets.fee (value, currency)
VALUES(5, 'EURO');

--EVENTS
INSERT INTO see_tickets.events ("name", fee_id)
VALUES('first event', 1);
INSERT INTO see_tickets.events ("name", fee_id)
VALUES('second event', 1);
INSERT INTO see_tickets.events ("name", fee_id)
VALUES('third event', 2);

--PRODUCTS
INSERT INTO see_tickets.products ("name", fee_id)
VALUES('apple', 1);
INSERT INTO see_tickets.products ("name", fee_id)
VALUES('banana', 1);
INSERT INTO see_tickets.products ("name", fee_id)
VALUES('strawberry', 2);
INSERT INTO see_tickets.products ("name", fee_id)
VALUES('lemon', 2);

--EVENT_PRODUCT
INSERT INTO see_tickets.event_product (event_id, product_id)
VALUES(1, 1);
INSERT INTO see_tickets.event_product (event_id, product_id)
VALUES(1, 2);
INSERT INTO see_tickets.event_product (event_id, product_id)
VALUES(1, 3);

INSERT INTO see_tickets.event_product (event_id, product_id)
VALUES(2, 1);
INSERT INTO see_tickets.event_product (event_id, product_id)
VALUES(2, 2);
INSERT INTO see_tickets.event_product (event_id, product_id)
VALUES(2, 3);
INSERT INTO see_tickets.event_product (event_id, product_id)
VALUES(2, 4);

INSERT INTO see_tickets.event_product (event_id, product_id)
VALUES(3, 3);
INSERT INTO see_tickets.event_product (event_id, product_id)
VALUES(3, 4);
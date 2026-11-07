-- Table: transactions_ejercicio1.products_bills

-- DROP TABLE IF EXISTS transactions_ejercicio1.products_bills;

CREATE TABLE IF NOT EXISTS transactions_ejercicio1.products_bills
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    product_id integer NOT NULL,
    bill_id integer NOT NULL,
    quantity integer,
    CONSTRAINT products_bills_pkey PRIMARY KEY (id),
    CONSTRAINT bill_id_fk FOREIGN KEY (bill_id)
        REFERENCES transactions_ejercicio1.bills (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT product_id_fk FOREIGN KEY (product_id)
        REFERENCES transactions_ejercicio1.products (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS transactions_ejercicio1.products_bills
    OWNER to postgres;
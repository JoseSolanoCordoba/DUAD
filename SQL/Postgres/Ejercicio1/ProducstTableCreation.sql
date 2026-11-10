-- Table: transactions_ejercicio1.products

-- DROP TABLE IF EXISTS transactions_ejercicio1.products;

CREATE TABLE IF NOT EXISTS transactions_ejercicio1.products
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    product_name character varying(30) COLLATE pg_catalog."default",
    stock integer NOT NULL,
    cost numeric(10,2),
    CONSTRAINT products_pkey PRIMARY KEY (id),
    CONSTRAINT stock_column_always_positive CHECK (stock >= 0)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS transactions_ejercicio1.products
    OWNER to postgres;
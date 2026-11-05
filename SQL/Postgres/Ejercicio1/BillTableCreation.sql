-- Table: transactions_ejercicio1.bills

-- DROP TABLE IF EXISTS transactions_ejercicio1.bills;

CREATE TABLE IF NOT EXISTS transactions_ejercicio1.bills
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    user_id integer NOT NULL,
    total numeric(10,2),
    state character(10) COLLATE pg_catalog."default",
    CONSTRAINT bills_pkey PRIMARY KEY (id),
    CONSTRAINT user_id_foreign_key FOREIGN KEY (user_id)
        REFERENCES transactions_ejercicio1.users (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS transactions_ejercicio1.bills
    OWNER to postgres;
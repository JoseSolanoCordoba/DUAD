-- Table: transactions_ejercicio1.users

-- DROP TABLE IF EXISTS transactions_ejercicio1.users;

CREATE TABLE IF NOT EXISTS transactions_ejercicio1.users
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    username character varying(30) COLLATE pg_catalog."default" NOT NULL,
    email character varying(30) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT users_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS transactions_ejercicio1.users
    OWNER to postgres;
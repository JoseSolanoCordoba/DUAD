set search_path TO transactions_ejercicio1;
DO $$
DECLARE
    -- Definimos variables para almacenar datos durante la ejecución
	v_total_cost DECIMAL;
	v_user_id INTEGER;
	v_bill_id INTEGER;
	
BEGIN
	-- Verificando existencia del stock de varios productos
	IF EXISTS (
	    SELECT 1
	    FROM (VALUES
 	       	(1, 5),
	        (2, 2),
	        (3, 1)
	    ) AS requested(product_id, quantity)
	    LEFT JOIN products AS p
 	       ON p.id = requested.product_id
 	   WHERE p.id IS NULL
		 OR p.stock IS NULL
  	     OR p.stock < requested.quantity
	) THEN
	    RAISE EXCEPTION 'Stock insuficiente o producto inexistente. Abortando transacción.';
	END IF;

	-- Verificando si el cliente existe en la base de datos
	IF NOT EXISTS (
		SELECT 1
		FROM users
		WHERE id = 4
	) THEN
		RAISE EXCEPTION 'El usuario no existe en transactions. Abortando transacción.';
	END IF;

	-- Almacenando 
	SELECT id INTO v_user_id
	FROM users
	WHERE id = 4;
	
	-- Sumando los costos
	SELECT SUM(p.cost * requested.quantity)
	INTO v_total_cost
	FROM products AS p
	JOIN (VALUES
	    (1, 2),
	    (2, 5),
	    (3, 1)
	) AS requested(product_id, quantity)
	ON p.id = requested.product_id;
	
	-- 2. Si hay stock y el cliente existe en la base de datos, procedemos a crear la orden
    INSERT INTO bills (user_id, total, state)
    VALUES (v_user_id, v_total_cost, 'Completed')
	RETURNING id INTO v_bill_id;

	-- Relacionando cantidad de productos y facturas.
	INSERT INTO products_bills (product_id, bill_id, quantity)
	VALUES
	(1, v_bill_id, 2),
	(2, v_bill_id, 5),
	(3, v_bill_id, 1);
	
	-- 3. Actualizamos el stock inmediatamente
	UPDATE products AS p
	SET stock = p.stock - requested.quantity
	FROM (VALUES
    	(1, 2),
    	(2, 5),
    	(3, 1)
	) AS requested(product_id, quantity)
	WHERE p.id = requested.product_id;

    RAISE NOTICE 'Orden creada.';
END $$;
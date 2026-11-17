set search_path TO transactions_ejercicio1;
DO $$
DECLARE
    -- Definimos variables para almacenar datos durante la ejecución
	v_user_id INTEGER;
	v_bill_id INTEGER;
	v_product_cost DECIMAL;
	v_total_cost DECIMAL := 0;
	v_product INTEGER[];
	-- Creación de productos y cantidades solicitadas por el cliente en un array:
	v_cart INTEGER[][] := ARRAY[
    [1, 5],
    [2, 2],
    [3, 1]
];
	
BEGIN

	-- Verificando si el cliente existe en la base de datos
	IF NOT EXISTS (
		SELECT 1
		FROM users
		WHERE id = 7
	) THEN
		RAISE EXCEPTION 'El usuario no existe en transactions. Abortando transacción.';
	END IF;

	-- Almacenando id de cliente en variable para su uso posterior
	SELECT id INTO v_user_id
	FROM users
	WHERE id = 7;

	-- Bucle para verificaciones varias por producto y cantidad de ese producto
	FOREACH v_product SLICE 1 IN ARRAY v_cart
	LOOP
	-- Verificando existencia del stock de varios productos
        IF NOT EXISTS (
            SELECT 1
            FROM products
            WHERE id = v_product[1]
              AND stock IS NOT NULL
              AND stock >= v_product[2]
        ) THEN
            RAISE EXCEPTION
                'Stock insuficiente o producto inexistente. Abortando transacción.';
        END IF;
	
		-- Sumando los costos
		SELECT cost INTO v_product_cost
		FROM products
		WHERE id = v_product[1];
		v_total_cost := v_total_cost + v_product_cost * v_product[2];

		-- Actualizamos el stock inmediatamente
		UPDATE products AS p
		SET stock = p.stock - v_product[2]
		WHERE p.id = v_product[1];
		
	END LOOP;

	-- Si hay stock y el cliente existe en la base de datos, procedemos a crear la orden
    INSERT INTO bills (user_id, total, state)
    VALUES (v_user_id, v_total_cost, 'Completed')
	RETURNING id INTO v_bill_id;

	-- Relacionando cantidad de productos y facturas.
	FOREACH v_product SLICE 1 IN ARRAY v_cart
	LOOP
		INSERT INTO products_bills (product_id, bill_id, quantity)
		VALUES
		(v_product[1], v_bill_id, v_product[2]);
	END LOOP;

	
    RAISE NOTICE 'Orden creada.';
END $$;
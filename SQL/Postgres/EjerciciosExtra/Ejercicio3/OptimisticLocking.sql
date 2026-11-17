set search_path TO transactions_ejercicio1;
DO $$
DECLARE
    -- Definimos variables para almacenar datos durante la ejecución
	v_user_id INTEGER;
	v_bill_id INTEGER;
	v_current_stock INTEGER;
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
	 
		-- Almacenando stock actual en variable
       	SELECT stock INTO v_current_stock
		FROM products
		WHERE id = v_product[1];

		-- Chequeando existencia de stock antes de proceder
		IF NOT FOUND OR
			v_current_stock IS NULL OR
			v_current_stock < v_product[2]
		THEN
			RAISE EXCEPTION 'Producto inexistente o stock insuficiente';
		END IF;
		
		-- Sumando los costos
		SELECT cost INTO v_product_cost
		FROM products
		WHERE id = v_product[1];
		v_total_cost := v_total_cost + v_product_cost * v_product[2];

		-- Compra ficticia realizada por otro cliente
		UPDATE products AS p
		SET stock = p.stock - v_product[2]
		WHERE p.id = v_product[1];

		-- Actualizamos el stock con bloqueo optimista
		UPDATE products AS p
		SET stock = p.stock - v_product[2]
		WHERE p.id = v_product[1]
			AND stock = v_current_stock;

		-- Verificando si el stock cambió
		IF NOT FOUND THEN
		    RAISE EXCEPTION
		        'El stock cambió durante la compra y existencia insuficiente. Abortando transacción.';
		END IF;
		
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
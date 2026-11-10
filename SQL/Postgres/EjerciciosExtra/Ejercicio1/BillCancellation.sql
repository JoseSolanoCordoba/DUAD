set search_path TO transactions_ejercicio1;
DO $$
DECLARE
    -- Definimos variables para almacenar datos durante la ejecución
	v_user_id INTEGER;
	v_bill_id INTEGER;
	v_product_cost DECIMAL;
	v_total_cost DECIMAL := 0;
	v_shipping_address VARCHAR(255);
	v_delivered BOOLEAN := TRUE;
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
    VALUES (v_user_id, v_total_cost, 'Pending')
	RETURNING id INTO v_bill_id;
	
	RAISE NOTICE 'Orden creada.';

	-- Relacionando cantidad de productos y facturas.
	FOREACH v_product SLICE 1 IN ARRAY v_cart
	LOOP
		INSERT INTO products_bills (product_id, bill_id, quantity)
		VALUES
		(v_product[1], v_bill_id, v_product[2]);
	END LOOP;

	-- Bloque de shipping para hacer checkpoint
	-- Generando entrega de productos.
	BEGIN
	    -- 4.1. Intentamos generar el envío
        INSERT INTO shipping (bill_id, address, status)
        VALUES (v_bill_id, '123 Main St', 'Pending');

        -- 4.3. Validación de dirección
        SELECT address INTO v_shipping_address
        FROM shipping
        WHERE bill_id = v_bill_id;
        
        -- Si la dirección es inválida, forzamos un error
        IF v_shipping_address = '' OR v_shipping_address IS NULL THEN
          RAISE EXCEPTION 'Error en dirección de envío';
        END IF;

		-- Actualizando estado de entrega de productos
		FOREACH v_product SLICE 1 IN ARRAY v_cart
		LOOP
		    UPDATE products_bills
		    SET delivered = v_delivered
		    WHERE bill_id = v_bill_id
		      AND product_id = v_product[1];

		    v_delivered := NOT v_delivered;
		END LOOP;
		
        RAISE NOTICE 'Envío de productos completado.';
	EXCEPTION
	   WHEN OTHERS THEN
            RAISE NOTICE 'Error en envío/cliente: %. Orden e inventario YA fueron procesados.', SQLERRM;
			RAISE;
	END;


	-- Bloque encargado de cancelar la factura, si todos los productos fueron entregados, la marca como
	-- completada.
	BEGIN
		-- Verificando entrega de productos
        IF NOT EXISTS (
            SELECT 1
            FROM products_bills
            WHERE bill_id = v_bill_id
              AND delivered = FALSE
        ) THEN
			-- Cambiando estado de la factura
			UPDATE bills AS b
			SET state = 'Completada'
			WHERE b.id = v_bill_id;
				RAISE NOTICE 'Factura completada con todos los productos entregados.';
				RETURN;
        END IF;
		
		-- Verificando que la factura no haya sido retornada
		IF EXISTS (
			SELECT 1
			FROM bills
			WHERE id = v_bill_id
				AND state = 'Retornada'
		) THEN
			RAISE EXCEPTION 'La factura ya fue retornada. Abortando transacción.';
		END IF;

		-- Cambiando estado de la factura
		UPDATE bills AS b
		SET state = 'Retornada'
		WHERE id = v_bill_id;
			
		-- Aumentando la cantidad de productos por producto que había en la factura.
		UPDATE products AS p
		SET stock = p.stock + pb.quantity
		FROM products_bills AS pb
		WHERE p.id = pb.product_id
			AND pb.bill_id = v_bill_id
			AND pb.delivered = FALSE;

	    RAISE NOTICE 'Factura cancelada y stock revertido de productos no entregados.';
		
	EXCEPTION
		WHEN OTHERS THEN
			RAISE NOTICE 'Error: %', SQLERRM;
	END;

END $$;
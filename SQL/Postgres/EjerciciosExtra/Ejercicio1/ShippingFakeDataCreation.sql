set search_path TO transactions_ejercicio1;
DO $$
DECLARE
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
	-- Bloque de shipping para hacer checkpoint
	-- Generando entrega de productos.
	BEGIN
		-- Verificando existencia de la factura a la que se va realizar envío
		IF NOT EXISTS (
            SELECT 1
            FROM bills
            WHERE id = 28
        ) THEN
            RAISE EXCEPTION
                'No existe la factura.';
        END IF;
	
	    -- 4.1. Intentamos generar el envío
        INSERT INTO shipping (bill_id, address, status)
        VALUES (28, '123 Main St', 'Pending');

        -- 4.3. Validación de dirección
        SELECT address INTO v_shipping_address
        FROM shipping
        WHERE bill_id = 28;
        
        -- Si la dirección es inválida, forzamos un error
        IF v_shipping_address = '' OR v_shipping_address IS NULL THEN
          RAISE EXCEPTION 'Error en dirección de envío';
        END IF;

		-- Actualizando estado de entrega de productos
		FOREACH v_product SLICE 1 IN ARRAY v_cart
		LOOP
		    UPDATE products_bills
		    SET delivered = v_delivered
		    WHERE bill_id = 28
		      AND product_id = v_product[1];

		    v_delivered := NOT v_delivered;
		END LOOP;
		
        RAISE NOTICE 'Envío de productos completado.';
	EXCEPTION
	   WHEN OTHERS THEN
			RAISE;
	END;
END $$;
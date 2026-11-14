set search_path TO transactions_ejercicio1;
DO $$
DECLARE
    -- Definimos variables para almacenar datos durante la ejecución
	v_bill_id INTEGER := 10;
	v_actual_bill_state VARCHAR(10);
	
BEGIN
	-- Bloque encargado de cancelar la factura, si todos los productos fueron entregados, la marca como
	-- completada.
	BEGIN
		SELECT state INTO v_actual_bill_state
		FROM bills
		WHERE id = v_bill_id;
		
		IF NOT FOUND THEN
		RAISE EXCEPTION 'La factura no existe';
		END IF;
		
		IF v_actual_bill_state = 'Pending'
		THEN 			
			-- Verificando entrega de productos
	        IF NOT EXISTS (
	            SELECT 1
	            FROM products_bills
	            WHERE bill_id = v_bill_id
	              AND delivered = FALSE
	        ) THEN
				-- Cambiando estado de la factura
				UPDATE bills AS b
				SET state = 'Completed'
				WHERE b.id = v_bill_id;
					RAISE NOTICE 'Factura completada con todos los productos entregados.';
					RETURN;
	        END IF;
			
			-- Aumentando la cantidad de productos por producto que había en la factura.
			UPDATE products AS p
			SET stock = p.stock + pb.quantity
			FROM products_bills AS pb
			WHERE p.id = pb.product_id
				AND pb.bill_id = v_bill_id
				AND pb.delivered = FALSE;
				
			-- Cambiando estado de la factura
			UPDATE bills AS b
			SET state = 'Cancelled'
			WHERE b.id = v_bill_id;
			
			RAISE NOTICE 'Factura cancelada y stock revertido de productos no entregados.';
		END IF;
				
	EXCEPTION
		WHEN OTHERS THEN
			RAISE;
	END;

END $$;
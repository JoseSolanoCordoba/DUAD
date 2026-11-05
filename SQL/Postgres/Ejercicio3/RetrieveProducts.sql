set search_path TO transactions_ejercicio1;
DO $$
DECLARE
    -- Definimos variables para almacenar datos durante la ejecución
	v_total_cost DECIMAL;
	v_user_id INTEGER;
	v_bill_id INTEGER;
	
BEGIN
	-- 1. Verificando si la factura existe en la base de datos
	IF NOT EXISTS (
		SELECT 1
		FROM bills
		WHERE id = 8
	) THEN
		RAISE EXCEPTION 'La factura no existe en bills. Abortando transacción.';
	END IF;

	-- 2. Aumentando la cantidad de productos por producto que había en la factura.
	UPDATE products AS p
	SET stock = p.stock + pb.quantity
	FROM products_bills AS pb
	WHERE p.id = pb.product_id
		AND pb.bill_id = 8;

	-- 3. Cambiando estado de la factura
	UPDATE bills AS b
	SET state = 'Retornada'
	WHERE id = 8;
	
    RAISE NOTICE 'Orden creada.';
END $$;
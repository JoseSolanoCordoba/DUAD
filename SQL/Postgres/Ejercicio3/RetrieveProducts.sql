set search_path TO transactions_ejercicio1;
DO $$
DECLARE

BEGIN
	-- 1. Verificando si la factura existe en la base de datos
	IF NOT EXISTS (
		SELECT 1
		FROM bills
		WHERE id = 15
	) THEN
		RAISE EXCEPTION 'La factura no existe en bills. Abortando transacción.';
	END IF;

	-- 2.Verificando que la factura no haya sido retornada
	IF EXISTS (
		SELECT 1
		FROM bills
		WHERE id = 15
			AND state = 'Retornada'
	) THEN
		RAISE EXCEPTION 'La factura ya fue retornada. Abortando transacción.';
	END IF;


	-- 3. Aumentando la cantidad de productos por producto que había en la factura.
	UPDATE products AS p
	SET stock = p.stock + pb.quantity
	FROM products_bills AS pb
	WHERE p.id = pb.product_id
		AND pb.bill_id = 15;

	-- 4. Cambiando estado de la factura
	UPDATE bills AS b
	SET state = 'Retornada'
	WHERE id = 15;
	
    RAISE NOTICE 'Orden retornada.';
END $$;
--------------------------------------------------
-- Función
--------------------------------------------------

CREATE OR REPLACE FUNCTION fn_validar_stock()

RETURNS TRIGGER

AS $$

DECLARE

    v_stock INT;

BEGIN

    SELECT stock

    INTO v_stock

    FROM producto

    WHERE id_producto = NEW.id_producto;


    IF NEW.cantidad > v_stock THEN

        RAISE EXCEPTION

        'Stock insuficiente';

    END IF;


    RETURN NEW;

END;

$$ LANGUAGE plpgsql;



--------------------------------------------------
-- Trigger
--------------------------------------------------

CREATE TRIGGER trg_validar_stock

BEFORE INSERT

ON detalle_pedido

FOR EACH ROW

EXECUTE FUNCTION fn_validar_stock();
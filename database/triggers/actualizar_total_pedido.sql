--------------------------------------------------
-- Función
--------------------------------------------------

CREATE OR REPLACE FUNCTION fn_actualizar_total()

RETURNS TRIGGER

AS $$

BEGIN

    UPDATE pedido

    SET total = (

        SELECT COALESCE(SUM(subtotal),0)

        FROM detalle_pedido

        WHERE id_pedido = NEW.id_pedido

    )

    WHERE id_pedido = NEW.id_pedido;

    RETURN NEW;

END;

$$ LANGUAGE plpgsql;



--------------------------------------------------
-- Trigger
--------------------------------------------------

CREATE TRIGGER trg_actualizar_total

AFTER INSERT OR UPDATE

ON detalle_pedido

FOR EACH ROW

EXECUTE FUNCTION fn_actualizar_total();
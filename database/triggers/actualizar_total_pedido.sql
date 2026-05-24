--------------------------------------------------
-- Función
--------------------------------------------------
-- Propósito: Mantener actualizado el valor acumulado del campo 'total' en la 
-- tabla 'pedido' cada vez que se añadan o modifiquen platos/bebidas al detalle.

CREATE OR REPLACE FUNCTION fn_actualizar_total()

RETURNS TRIGGER

AS $$

BEGIN

    -- Actualiza el pedido principal sumando el precio * cantidad del nuevo ítem.
    -- Implementa una actualización reactiva en cascada para evitar desincronizaciones de totales.

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
--------------------------------------------------
-- Función
--------------------------------------------------
-- Propósito: Garantizar la consistencia transaccional del inventario antes 
-- de confirmar la inserción de un ítem en un pedido.

CREATE OR REPLACE FUNCTION fn_validar_stock()

RETURNS TRIGGER

AS $$

DECLARE

    v_stock INT;

BEGIN

    -- Obtenemos el stock del producto que se está intentando pedir

    SELECT stock

    INTO v_stock

    FROM producto

    WHERE id_producto = NEW.id_producto;

   -- Validamos si el producto existe

    IF NOT FOUND THEN
        RAISE EXCEPTION 'El producto con ID % no existe.', NEW.ID_producto;
    END IF;

    -- REGLA DE NEGOCIO: Validar si la cantidad pedida supera el stock

    IF NEW.cantidad > v_stock THEN

        RAISE EXCEPTION

        'Stock insuficiente para el producto con ID %.', NEW.ID_producto;

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

-- Cláusula WHEN: Solo ejecutamos el trigger si están pidiendo más de 0 unidades.
-- Esto filtra casos irrelevantes (ej: actualizaciones de precio o fecha donde la cantidad no cambia o es nula)

WHEN (NEW.cantidad_pedida > 0)

EXECUTE FUNCTION fn_validar_stock();
-- TRIGGER: trg_audit_pedido
-- Se dispara AFTER INSERT, UPDATE o DELETE en la tabla pedido.
-- Registra en pedido_audit la operación realizada (I/U/D), el usuario
-- que la ejecutó, la marca de tiempo y los datos anteriores y nuevos
-- en formato JSONB, garantizando trazabilidad completa de los cambios.

CREATE OR REPLACE FUNCTION fn_audit_pedido()

RETURNS TRIGGER

AS $$

BEGIN

    -- INSERT: solo hay dato nuevo
    IF (TG_OP = 'INSERT') THEN

        INSERT INTO pedido_audit(
            operacion,
            usuario,
            dato_viejo,
            dato_nuevo,
            id_pedido
        )
        VALUES (
            'I',
            current_user,
            NULL,
            row_to_json(NEW),
            NEW.id_pedido
        );

        RETURN NEW;

    -- UPDATE: hay dato viejo y dato nuevo
    ELSIF (TG_OP = 'UPDATE') THEN

        INSERT INTO pedido_audit(
            operacion,
            usuario,
            dato_viejo,
            dato_nuevo,
            id_pedido
        )
        VALUES (
            'U',
            current_user,
            row_to_json(OLD),
            row_to_json(NEW),
            NEW.id_pedido
        );

        RETURN NEW;

    -- DELETE: solo hay dato viejo
    ELSIF (TG_OP = 'DELETE') THEN

        INSERT INTO pedido_audit(
            operacion,
            usuario,
            dato_viejo,
            dato_nuevo,
            id_pedido
        )
        VALUES (
            'D',
            current_user,
            row_to_json(OLD),
            NULL,
            OLD.id_pedido
        );

        RETURN OLD;

    END IF;

END;

$$ LANGUAGE plpgsql;



CREATE TRIGGER trg_audit_pedido

AFTER INSERT OR UPDATE OR DELETE

ON pedido

FOR EACH ROW

EXECUTE FUNCTION fn_audit_pedido();

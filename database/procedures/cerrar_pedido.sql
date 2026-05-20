CREATE OR REPLACE PROCEDURE cerrar_pedido(

    p_id_pedido INT

)

LANGUAGE plpgsql

AS $$

DECLARE

    v_existe INT;

BEGIN

    ------------------------------------
    -- Verificar si pedido existe
    ------------------------------------

    SELECT COUNT(*)

    INTO v_existe

    FROM pedido

    WHERE id_pedido = p_id_pedido;


    IF v_existe = 0 THEN

        RAISE EXCEPTION
        'Pedido no existe';

    END IF;


    ------------------------------------
    -- Cambiar estado pedido
    ------------------------------------

    UPDATE pedido

    SET estado = 'finalizado'

    WHERE id_pedido = p_id_pedido;


    RAISE NOTICE
    'Pedido cerrado correctamente';

END;

$$;
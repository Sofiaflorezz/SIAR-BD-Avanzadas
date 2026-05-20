CREATE OR REPLACE PROCEDURE registrar_reserva(

    p_id_cliente INT,
    p_id_mesa INT,
    p_fecha DATE,
    p_hora TIME

)

LANGUAGE plpgsql

AS $$

DECLARE

    v_existe INT;

BEGIN

    ------------------------------------------------
    -- Verificar si mesa ya está reservada
    ------------------------------------------------

    SELECT COUNT(*)

    INTO v_existe

    FROM reserva

    WHERE id_mesa = p_id_mesa
    AND fecha_reserva = p_fecha
    AND hora_reserva = p_hora
    AND estado = 'confirmada';


    IF v_existe > 0 THEN

        RAISE EXCEPTION
        'La mesa ya está reservada';

    END IF;


    ------------------------------------------------
    -- Crear reserva
    ------------------------------------------------

    INSERT INTO reserva(

        id_cliente,
        id_mesa,
        fecha_reserva,
        hora_reserva,
        estado

    )

    VALUES(

        p_id_cliente,
        p_id_mesa,
        p_fecha,
        p_hora,
        'confirmada'

    );


    RAISE NOTICE
    'Reserva registrada correctamente';

END;

$$;
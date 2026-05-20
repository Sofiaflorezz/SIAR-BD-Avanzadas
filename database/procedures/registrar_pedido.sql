CREATE OR REPLACE PROCEDURE registrar_pedido(

    p_id_cliente INT,
    p_id_mesa INT,
    p_id_producto INT,
    p_cantidad INT,
    p_metodo_pago VARCHAR

)

LANGUAGE plpgsql

AS $$

DECLARE

    v_id_pedido INT;
    v_precio NUMERIC;
    v_subtotal NUMERIC;

BEGIN

    --------------------------------------------------
    -- Obtener precio del producto
    --------------------------------------------------

    SELECT precio
    INTO v_precio
    FROM producto
    WHERE id_producto = p_id_producto;


    IF v_precio IS NULL THEN
        RAISE EXCEPTION
        'Producto % no existe',
        p_id_producto;
    END IF;


    --------------------------------------------------
    -- Calcular subtotal
    --------------------------------------------------

    v_subtotal := v_precio * p_cantidad;


    --------------------------------------------------
    -- Crear pedido
    --------------------------------------------------

    INSERT INTO pedido(

        id_cliente,
        id_mesa,
        fecha_pedido,
        estado,
        total

    )

    VALUES(

        p_id_cliente,
        p_id_mesa,
        NOW(),
        'pendiente',
        v_subtotal

    )

    RETURNING id_pedido

    INTO v_id_pedido;


    --------------------------------------------------
    -- Crear detalle pedido
    --------------------------------------------------

    INSERT INTO detalle_pedido(

        id_pedido,
        id_producto,
        cantidad,
        precio_unitario,
        subtotal

    )

    VALUES(

        v_id_pedido,
        p_id_producto,
        p_cantidad,
        v_precio,
        v_subtotal

    );


    --------------------------------------------------
    -- Crear factura
    --------------------------------------------------

    INSERT INTO factura(

        id_pedido,
        fecha_factura,
        total_precio,
        metodo_pago

    )

    VALUES(

        v_id_pedido,
        NOW(),
        v_subtotal,
        p_metodo_pago

    );


    RAISE NOTICE
    'Pedido registrado correctamente. ID=%',
    v_id_pedido;

END;

$$;
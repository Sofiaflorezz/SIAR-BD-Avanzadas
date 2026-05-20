from app.config.db import get_connection


def agregar_producto_pedido(
        id_pedido,
        id_producto,
        cantidad
):

    conn = get_connection()
    cursor = conn.cursor()

    # buscar producto
    cursor.execute(
        """
        SELECT precio, stock
        FROM productos
        WHERE id_producto=%s
        """,
        (id_producto,)
    )

    producto = cursor.fetchone()

    if producto is None:

        cursor.close()
        conn.close()

        return "producto_no_existe"

    precio = producto[0]
    stock = producto[1]

    # validar stock
    if stock < cantidad:

        cursor.close()
        conn.close()

        return "stock_insuficiente"

    subtotal = precio * cantidad

    # insertar detalle pedido
    cursor.execute(
        """
        INSERT INTO detalle_pedido(
            id_pedido,
            id_producto,
            cantidad,
            subtotal
        )
        VALUES(%s,%s,%s,%s)
        """,
        (
            id_pedido,
            id_producto,
            cantidad,
            subtotal
        )
    )

    # descontar stock
    cursor.execute(
        """
        UPDATE productos
        SET stock = stock - %s
        WHERE id_producto=%s
        """,
        (
            cantidad,
            id_producto
        )
    )

    # actualizar total pedido
    cursor.execute(
        """
        UPDATE pedidos
        SET total = (
            SELECT COALESCE(
                SUM(subtotal),
                0
            )
            FROM detalle_pedido
            WHERE id_pedido=%s
        )
        WHERE id_pedido=%s
        """,
        (
            id_pedido,
            id_pedido
        )
    )

    conn.commit()

    cursor.close()
    conn.close()

    return subtotal
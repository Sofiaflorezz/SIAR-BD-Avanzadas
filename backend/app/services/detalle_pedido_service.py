from app.config.db import get_connection


def agregar_producto_pedido(
        id_pedido,
        id_producto,
        cantidad
):

    conn = get_connection()
    cursor = conn.cursor()


    # Buscar producto
    cursor.execute("""

        SELECT precio, stock

        FROM producto

        WHERE id_producto=%s

    """, (id_producto,))

    producto = cursor.fetchone()


    # Validar producto existente
    if not producto:

        cursor.close()
        conn.close()

        return "producto_no_existe"


    precio = float(producto[0])
    stock = int(producto[1])


    # Validar stock suficiente
    if cantidad > stock:

        cursor.close()
        conn.close()

        return "stock_insuficiente"


    # Calcular subtotal
    subtotal = precio * cantidad


    # Insertar detalle pedido
    cursor.execute("""

        INSERT INTO detalle_pedido(

            id_pedido,
            id_producto,
            cantidad,
            precio_unitario,
            subtotal

        )

        VALUES(%s,%s,%s,%s,%s)

    """, (

        id_pedido,
        id_producto,
        cantidad,
        precio,
        subtotal

    ))


    # Descontar stock
    cursor.execute("""

        UPDATE producto

        SET stock = stock - %s

        WHERE id_producto=%s

    """, (

        cantidad,
        id_producto

    ))


    # Actualizar total pedido
    cursor.execute("""

        UPDATE pedido

        SET total=(

            SELECT COALESCE(
                SUM(subtotal),
                0
            )

            FROM detalle_pedido

            WHERE id_pedido=%s

        )

        WHERE id_pedido=%s

    """, (

        id_pedido,
        id_pedido

    ))


    conn.commit()

    cursor.close()
    conn.close()


    return subtotal
from app.config.db import get_connection


# ==========================
# CREAR PEDIDO
# ==========================

def create_pedido(id_cliente, id_mesa=None):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO pedido(
            id_cliente,
            id_mesa,
            total
        )

        VALUES(%s,%s,0)

        RETURNING id_pedido
        """,
        (
            id_cliente,
            id_mesa
        )
    )

    pedido_id = cursor.fetchone()[0]

    conn.commit()

    cursor.close()
    conn.close()

    return pedido_id


# ==========================
# OBTENER PEDIDO POR ID
# ==========================

def get_pedido_by_id(id_pedido):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT

            p.id_pedido,
            p.id_cliente,
            p.total,

            pr.nombre,

            d.cantidad,
            d.subtotal

        FROM pedido p

        LEFT JOIN detalle_pedido d
            ON p.id_pedido = d.id_pedido

        LEFT JOIN producto pr
            ON d.id_producto = pr.id_producto

        WHERE p.id_pedido = %s
        """,
        (id_pedido,)
    )

    datos = cursor.fetchall()

    cursor.close()
    conn.close()

    return datos


# ==========================
# OBTENER TODOS LOS PEDIDOS
# ==========================

def get_pedidos():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT

            id_pedido,
            id_cliente,
            total,
            estado

        FROM pedido

        ORDER BY id_pedido
        """
    )

    pedidos = cursor.fetchall()

    cursor.close()
    conn.close()

    return pedidos
def cerrar_pedido(id_pedido):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

        UPDATE pedido
        SET estado = 'cerrado'
        WHERE id_pedido = %s

        RETURNING total

    """, (id_pedido,))

    result = cursor.fetchone()

    conn.commit()
    cursor.close()
    conn.close()

    if not result:
        return None

    return result[0]

def crear_factura(id_pedido):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO factura (
            id_pedido,
            total_precio,
            metodo_pago
        )
        SELECT
            id_pedido,
            total,
            'efectivo'
        FROM pedido
        WHERE id_pedido = %s
        RETURNING id_factura
    """, (id_pedido,))

    factura_id = cursor.fetchone()[0]

    conn.commit()
    cursor.close()
    conn.close()

    return factura_id
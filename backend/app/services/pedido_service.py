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
            id_mesa,   
            total,
            estado
        FROM pedido
        ORDER BY id_pedido DESC
        """
    )
    pedidos = cursor.fetchall()
    cursor.close()
    conn.close()
    lista = []
    for pedido in pedidos:
        lista.append({
            "id_pedido": pedido[0],
            "id_cliente": pedido[1],
            "id_mesa": pedido[2],       
            "total": float(pedido[3]),
            "estado": pedido[4]
        })
    return lista

# ==========================
# FACTURAR PEDIDO
# Reemplaza cerrar_pedido y crear_factura.
# Ejecuta ambas operaciones en una sola transacción.
# Si algo falla, el ROLLBACK deshace los dos cambios.
# ==========================
def facturar_pedido(id_pedido):
    conn = get_connection()
    try:
        cursor = conn.cursor()

        # Verificar que el pedido existe y obtener el total
        cursor.execute("""
            SELECT total FROM pedido
            WHERE id_pedido = %s
        """, (id_pedido,))
        result = cursor.fetchone()

        if not result:
            return None, "Pedido no encontrado"

        total = result[0]

        # Cerrar el pedido
        cursor.execute("""
            UPDATE pedido
            SET estado = 'cerrado'
            WHERE id_pedido = %s
        """, (id_pedido,))

        # Crear la factura
        cursor.execute("""
            INSERT INTO factura (
                id_pedido,
                total_precio,
                metodo_pago
            )
            VALUES (%s, %s, 'efectivo')
            RETURNING id_factura
        """, (id_pedido, total))

        id_factura = cursor.fetchone()[0]

        # COMMIT — ambas operaciones se confirman juntas
        conn.commit()
        cursor.close()
        conn.close()
        return id_factura, None

    except Exception as e:
        # ROLLBACK — si algo falla se revierten los dos
        conn.rollback()
        conn.close()
        return None, str(e)

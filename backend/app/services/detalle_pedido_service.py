from app.config.db import get_connection

def agregar_producto_pedido(id_pedido, id_producto, cantidad):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        # Iniciar transacción explícita (Requisito R8)
        cursor.execute("BEGIN;")

        # buscar producto
        cursor.execute("SELECT precio, stock FROM producto WHERE id_producto=%s", (id_producto,))
        producto = cursor.fetchone()

        if producto is None:
            conn.rollback()
            return "producto_no_existe"

        precio = producto[0]
        stock = producto[1]

        # validar stock
        if stock < cantidad:
            conn.rollback()
            return "stock_insuficiente"

        subtotal = precio * cantidad

        # insertar detalle pedido (El trigger fn_actualizar_total se disparará aquí)
        cursor.execute(
            """
            INSERT INTO detalle_pedido(id_pedido, id_producto, cantidad, precio_unitario, subtotal)
            VALUES(%s,%s,%s,%s,%s)
            """,
            (id_pedido, id_producto, cantidad, precio, subtotal)
        )

        # descontar stock (Actualizado a la tabla 'producto' en singular según tu esquema 03)
        cursor.execute(
            "UPDATE producto SET stock = stock - %s WHERE id_producto=%s",
            (cantidad, id_producto)
        )

        conn.commit() # Consolidar transacción
        return subtotal

    except Exception as e:
        conn.rollback() # Revertir cambios en caso de error
        print(f"Error transaccional: {e}")
        return "error_transaccion"
        
    finally:
        cursor.close()
        conn.close()
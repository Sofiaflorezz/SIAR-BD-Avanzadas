from app.config.db import get_connection


# ==========================
# GET TODOS
# ==========================

def get_all_productos():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM producto
        ORDER BY id_producto;
    """)

    productos = cursor.fetchall()

    cursor.close()
    conn.close()

    resultado = []

    for producto in productos:

        resultado.append({

            "id_producto": producto[0],
            "nombre": producto[1],
            "detalle_producto": producto[2],
            "precio": float(producto[3]),
            "stock": producto[4]

        })

    return resultado


# ==========================
# GET POR ID
# ==========================

def get_producto_by_id(id_producto):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

        SELECT *
        FROM producto
        WHERE id_producto=%s

    """,(id_producto,))

    producto = cursor.fetchone()

    cursor.close()
    conn.close()

    if not producto:

        return None


    return {

        "id_producto": producto[0],
        "nombre": producto[1],
        "detalle_producto": producto[2],
        "precio": float(producto[3]),
        "stock": producto[4]

    }


# ==========================
# POST
# ==========================

def create_producto(
        nombre,
        detalle_producto,
        precio,
        stock
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

        INSERT INTO producto
        (
            nombre,
            detalle_producto,
            precio,
            stock
        )

        VALUES
        (%s,%s,%s,%s)

        RETURNING id_producto

    """,(

        nombre,
        detalle_producto,
        precio,
        stock

    ))

    id_producto = cursor.fetchone()[0]

    conn.commit()

    cursor.close()
    conn.close()

    return id_producto


# ==========================
# PUT
# ==========================

def update_producto(
        id_producto,
        nombre,
        detalle_producto,
        precio,
        stock
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

        UPDATE producto

        SET
            nombre=%s,
            detalle_producto=%s,
            precio=%s,
            stock=%s

        WHERE id_producto=%s

    """,(

        nombre,
        detalle_producto,
        precio,
        stock,
        id_producto

    ))

    conn.commit()

    cursor.close()
    conn.close()



# ==========================
# DELETE
# ==========================

def delete_producto(id_producto):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

        DELETE FROM producto
        WHERE id_producto=%s

    """,(id_producto,))

    conn.commit()

    cursor.close()
    conn.close()
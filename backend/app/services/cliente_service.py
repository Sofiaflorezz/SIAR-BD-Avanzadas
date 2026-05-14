from app.config.db import get_connection

def obtener_clientes():

    connection = get_connection()
    cursor = connection.cursor()

    query = "SELECT * FROM cliente"

    cursor.execute(query)

    clientes = cursor.fetchall()

    cursor.close()
    connection.close()

    return clientes
def obtener_cliente_por_id(id_cliente):

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        SELECT * FROM cliente
        WHERE id_cliente = %s
    """

    cursor.execute(query, (id_cliente,))

    cliente = cursor.fetchone()

    cursor.close()
    connection.close()

    return cliente
def insertar_cliente(nombre, telefono, correo, cedula):

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        INSERT INTO cliente(nombre, numero_telefono, correo, cedula)
        VALUES (%s, %s, %s, %s)
    """

    cursor.execute(query, (nombre, telefono, correo, cedula))

    connection.commit()

    cursor.close()
    connection.close()

def actualizar_cliente(id_cliente, nombre, telefono, correo, cedula):

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        UPDATE cliente
        SET nombre = %s,
            numero_telefono = %s,
            correo = %s,
            cedula = %s
        WHERE id_cliente = %s
    """

    cursor.execute(query, (
        nombre,
        telefono,
        correo,
        cedula,
        id_cliente
    ))

    connection.commit()

    cursor.close()
    connection.close()

def eliminar_cliente(id_cliente):

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        DELETE FROM cliente
        WHERE id_cliente = %s
    """

    cursor.execute(query, (id_cliente,))

    connection.commit()

    cursor.close()
    connection.close()

def existe_cliente(id_cliente):

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        SELECT * FROM cliente
        WHERE id_cliente = %s
    """

    cursor.execute(query, (id_cliente,))

    cliente = cursor.fetchone()

    cursor.close()
    connection.close()

    return cliente
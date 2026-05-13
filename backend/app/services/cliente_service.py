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
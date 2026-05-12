from app.config.db import get_connection

try:

    connection = get_connection()

    print("Conexión exitosa con PostgreSQL")

    connection.close()

except Exception as e:

    print("Error:")
    print(e)
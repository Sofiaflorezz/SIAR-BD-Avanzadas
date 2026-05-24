"""
Módulo de Configuración de Base de Datos.
Encargado de establecer y gestionar la conexión con PostgreSQL utilizando psycopg2.
"""

import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    """
    Establece una conexión con la base de datos PostgreSQL utilizando 
    las credenciales del archivo .env.
    
    Returns:
        connection: Objeto de conexión de psycopg2 si es exitosa.
        
    Raises:
        psycopg2.OperationalError: Si hay un fallo al intentar conectar con la BD.
    """
    connection = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")
    )

    return connection
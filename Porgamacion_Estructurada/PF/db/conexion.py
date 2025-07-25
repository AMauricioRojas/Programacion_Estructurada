# db/conexion.py
import mysql.connector
from mysql.connector import Error

def crear_conexion():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='bd_vegegym'
        )
        return conexion
    except Error as e:
        print(f"❌ Error de conexión a la base de datos: {e}")
        return None

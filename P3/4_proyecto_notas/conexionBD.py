import mysql.connector

conexion = None
cursor = None

try:
    conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="bd_notas"
    )
    cursor = conexion.cursor(buffered=True)
except Exception as e:
    print(f"Error al conectar con la base de datos: {e}")
    print("En este momento no es posible comunicarse con el sistema, inténtelo más tarde...")
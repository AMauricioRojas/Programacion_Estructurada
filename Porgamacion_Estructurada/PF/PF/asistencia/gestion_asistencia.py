# asistencia/gestion_asistencia.py
from db.conexion import crear_conexion
from datetime import datetime

def registrar_asistencia():
    id_cliente = input("🆔 ID del cliente: ")

    conexion = crear_conexion()
    if conexion:
        cursor = conexion.cursor()
        sql = "INSERT INTO asistencia (id_cliente, fecha_entrada) VALUES (%s, %s)"
        datos = (id_cliente, datetime.now())
        try:
            cursor.execute(sql, datos)
            conexion.commit()
            print("✅ Asistencia registrada.")
        except Exception as e:
            print(f"❌ Error al registrar asistencia: {e}")
        finally:
            cursor.close()
            conexion.close()

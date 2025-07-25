# rutinas/gestion_rutinas.py
from db.conexion import crear_conexion

def agregar_rutina():
    id_cliente = input("🆔 ID del cliente: ")
    descripcion = input("🏋️ Descripción de la rutina: ")
    duracion = input("⏱️ Duración (minutos): ")
    nivel = input("🎚️ Nivel (básico, intermedio, avanzado): ")

    conexion = crear_conexion()
    if conexion:
        cursor = conexion.cursor()
        sql = "INSERT INTO rutinas (id_cliente, descripcion, duracion, nivel) VALUES (%s, %s, %s, %s)"
        datos = (id_cliente, descripcion, duracion, nivel)
        try:
            cursor.execute(sql, datos)
            conexion.commit()
            print("✅ Rutina agregada.")
        except Exception as e:
            print(f"❌ Error al agregar rutina: {e}")
        finally:
            cursor.close()
            conexion.close()

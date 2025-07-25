# pagos/gestion_pagos.py
from db.conexion import crear_conexion
from datetime import datetime

def registrar_pago():
    id_cliente = input("🆔 ID del cliente: ")
    monto = input("💵 Monto pagado: ")
    estatus = input("📌 Estatus (pagado/pendiente): ")

    conexion = crear_conexion()
    if conexion:
        cursor = conexion.cursor()
        sql = "INSERT INTO pagos (id_cliente, monto, fecha_pago, estatus) VALUES (%s, %s, %s, %s)"
        datos = (id_cliente, monto, datetime.now().date(), estatus)
        try:
            cursor.execute(sql, datos)
            conexion.commit()
            print("✅ Pago registrado.")
        except Exception as e:
            print(f"❌ Error al registrar pago: {e}")
        finally:
            cursor.close()
            conexion.close()

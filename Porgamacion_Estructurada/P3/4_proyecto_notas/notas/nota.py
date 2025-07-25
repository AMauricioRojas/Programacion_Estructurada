from conexionBD import *
import datetime

def crear(usuario_id, titulo, descripcion):
    try:
        cursor.execute("INSERT INTO notas(usuario_id, titulo, descripcion, fecha) VALUES (%s, %s, %s, NOW())",(usuario_id, titulo, descripcion))
        conexion.commit()
        return True
    except Exception as e:
        print(f"Error al crear nota: {e}")
        return False
    
def mostrar(usuario_id):
    try:
        cursor.execute("SELECT id, titulo, descripcion, fecha FROM notas WHERE usuario_id=%s ORDER BY fecha DESC", (usuario_id,))
        return cursor.fetchall()
    except Exception as e:
        print(f"Error al mostrar notas: {e}")
        return []

def actualizar(nota_id, usuario_id, titulo, descripcion):
    try:
        cursor.execute("""
            UPDATE notas 
            SET titulo=%s, descripcion=%s, fecha=NOW() 
            WHERE id=%s AND usuario_id=%s
        """, (titulo, descripcion, nota_id, usuario_id))
        conexion.commit()
        return cursor.rowcount > 0
    except Exception as e:
        print(f"Error al actualizar nota: {e}")
        return False

def eliminar(nota_id, usuario_id):
    try:
        cursor.execute("DELETE FROM notas WHERE id=%s AND usuario_id=%s", (nota_id, usuario_id))
        conexion.commit()
        return cursor.rowcount > 0
    except Exception as e:
        print(f"Error al eliminar nota: {e}")
        return False
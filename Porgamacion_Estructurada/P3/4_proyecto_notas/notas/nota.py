from conexionBD import *
import datetime

def crear(usuario_id,titulo,descripcion):
    try:
        cursor.execute("insert into notas(usuario_id,titulo,descripcion,fecha) values (%s,%s,%s,NOW())", (usuario_id,titulo,descripcion))
        conexion.commit()
        return True
    except:
        return False
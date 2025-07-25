from conexionBD import *
import datetime 
import hashlib

def hash_password(contrasena):
    return hashlib.sha256(contrasena.encode()).hexdigest()

def registrar(nombre, apellidos, email, contrasena):
    try: 
        fecha = datetime.datetime.now().date()
        contrasena_hash = hash_password(contrasena)
        sql = "INSERT INTO usuarios(nombre, apellidos, email, password, fecha) VALUES (%s, %s, %s, %s, %s)"
        val = (nombre, apellidos, email, contrasena_hash, fecha)
        cursor.execute(sql, val)
        conexion.commit()
        return True
    except Exception as e:
        print(f"Error al registrar usuario: {e}")
        return False

def inicio_sesion(email, contrasena):
    try:
        contrasena_hash = hash_password(contrasena)
        sql = "SELECT id, nombre, apellidos FROM usuarios WHERE email=%s AND password=%s"
        val = (email, contrasena_hash)
        cursor.execute(sql, val)
        registro = cursor.fetchone()
        
        if registro:
            return registro
        else:
            return False
    except Exception as e:
        print(f"Error al iniciar sesión: {e}")
        return None
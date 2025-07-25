# usuarios/funciones_usuario.py
import hashlib
from db.conexion import crear_conexion

def encriptar_contrasena(contrasena):
    return hashlib.sha256(contrasena.encode()).hexdigest()

def registrar_usuario(nombre_completo, usuario, contrasena):
    conexion = crear_conexion()
    if conexion:
        cursor = conexion.cursor()
        sql = "INSERT INTO usuarios (nombre_completo, usuario, contrasena) VALUES (%s, %s, %s)"
        datos = (nombre_completo, usuario, encriptar_contrasena(contrasena))
        try:
            cursor.execute(sql, datos)
            conexion.commit()
            print("✅ Usuario registrado exitosamente.")
        except Exception as e:
            print(f"❌ Error al registrar usuario: {e}")
        finally:
            cursor.close()
            conexion.close()

def iniciar_sesion(usuario, contrasena):
    conexion = crear_conexion()
    if conexion:
        cursor = conexion.cursor()
        sql = "SELECT contrasena FROM usuarios WHERE usuario = %s"
        cursor.execute(sql, (usuario,))
        resultado = cursor.fetchone()
        if resultado and resultado[0] == encriptar_contrasena(contrasena):
            print("🔓 Inicio de sesión exitoso.")
            return True
        else:
            print("🔐 Usuario o contraseña incorrectos.")
            return False

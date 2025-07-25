# usuarios/login.py
from usuarios.funciones_usuario import registrar_usuario, iniciar_sesion

def menu_login():
    while True:
        print("\n🔐 MENÚ DE ACCESO 🔐")
        print("1. 📝 Registrar nuevo usuario")
        print("2. 🔓 Iniciar sesión")
        print("3. 🚪 Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("👤 Nombre completo: ")
            usuario = input("📛 Nombre de usuario: ")
            contrasena = input("🔑 Contraseña: ")
            registrar_usuario(nombre, usuario, contrasena)
        elif opcion == "2":
            usuario = input("📛 Usuario: ")
            contrasena = input("🔑 Contraseña: ")
            if iniciar_sesion(usuario, contrasena):
                return True  # Ingreso exitoso, se puede continuar con el sistema
        elif opcion == "3":
            print("👋 Saliendo del sistema de acceso...")
            return False
        else:
            print("❌ Opción no válida. Intenta de nuevo.")

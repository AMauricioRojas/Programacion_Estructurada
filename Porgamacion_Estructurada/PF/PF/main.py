# main.py

from usuarios.login import menu_login
from clientes.gestion_clientes import menu_clientes
from rutinas.gestion_rutinas import agregar_rutina  # por ahora solo agregar, luego ampliamos
from pagos.gestion_pagos import registrar_pago       # igual, luego podemos ampliar
from asistencia.gestion_asistencia import registrar_asistencia  # idem

def mostrar_menu_principal():
    while True:
        print("\n🏋️‍♂️ BIENVENIDO A VEGEGYM 🏋️‍♀️")
        print("1. 👥 Gestión de clientes")
        print("2. 📋 Gestión de rutinas")
        print("3. 💰 Gestión de pagos")
        print("4. 🕓 Registro de asistencia")
        print("5. 🚪 Salir del sistema")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            menu_clientes()
        elif opcion == "2":
            agregar_rutina()
        elif opcion == "3":
            registrar_pago()
        elif opcion == "4":
            registrar_asistencia()
        elif opcion == "5":
            print("👋 ¡Gracias por usar VEGEGYM! Hasta luego.")
            break
        else:
            print("❌ Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    if menu_login():
        mostrar_menu_principal()

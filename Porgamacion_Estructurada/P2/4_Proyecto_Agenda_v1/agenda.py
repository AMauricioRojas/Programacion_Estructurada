import os

def borrarPantalla():
    os.system("cls")

def esperarTecla():
    print("\n\t\t...Oprime una tecla para continuar...")
    input()

def menu_principal():
    print("\n\t..::: 📓 Sistema de Gestión de Agenda de Contactos :::..\n")
    print(" 1.- 📝 Agregar Contacto")
    print(" 2.- 👀 Mostrar todos los contactos")
    print(" 3.- 🔍 Buscar contacto por Nombre")
    print(" 4.- ✏️ Modificar Contacto")  # Nueva posición
    print(" 5.- 🚪 Salir")  # Salir ahora es 5
    opcion = input("\n\tElige una opción (1-5): ").strip()
    return opcion

def agregar_contacto(agenda):
    borrarPantalla()
    print("📝 Agregar Contactos")
    nombre = input("Nombre: ").upper().strip()
    if nombre in agenda:
        print("⚠️ Contacto existente")
    else:
        tel = input("📞 Teléfono: ").strip()
        email = input("📧 Email: ").upper().strip()
        agenda[nombre] = [tel, email]
        print("✅ Acción realizada con éxito")

def mostrar_contacto(agenda):
    borrarPantalla()
    print("👀 Mostrar Contactos")
    if not agenda:
        print("📭 No hay contactos")
    else:
        print(f"\n{'📛 Nombre':<15}{'📞 Teléfono':<15}{'📧 Email':<15}")
        print("-"*45)
        for nombre, datos in agenda.items():
            print(f"{nombre:<15}{datos[0]:<15}{datos[1]:<15}")
        print("-"*45)

def buscar_contacto(agenda):
    borrarPantalla()
    print("🔍 Buscar Contactos")
    if not agenda:
        print("📭 No hay contactos")
    else:
        nombre = input("Nombre: ").upper().strip()
        if nombre in agenda:
            print(f"\n{'📛 Nombre':<15}{'📞 Teléfono':<15}{'📧 Email':<15}")
            print("-"*45)
            print(f"{nombre:<15}{agenda[nombre][0]:<15}{agenda[nombre][1]:<15}")
            print("-"*45)
        else:
            print("❌ No existe el contacto")

def modificar_contacto(agenda):
    borrarPantalla()
    print("✏️ Modificar Contactos")
    if not agenda:
        print("📭 No hay contactos")
    else:
        nombre = input("Nombre: ").upper().strip()
        if nombre in agenda:
            print(f"\n{'📛 Nombre':<15}{'📞 Teléfono':<15}{'📧 Email':<15}")
            print("-"*45)
            print(f"{nombre:<15}{agenda[nombre][0]:<15}{agenda[nombre][1]:<15}")
            print("-"*45)
            resp = input("¿Deseas modificar el contacto? (Sí/No): ").lower().strip()
            if resp == "sí" or resp == "si":
                tel = input("📞 Nuevo Teléfono: ").strip()
                email = input("📧 Nuevo Email: ").upper().strip()
                agenda[nombre] = [tel, email]
                print("✅ Acción realizada con éxito")
        else:
            print("❌ No existe el contacto")
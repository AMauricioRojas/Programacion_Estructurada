import os

def borrarPantalla():
    os.system("cls")

def esperarTecla():
    input("\nPresiona Enter para continuar...")

def calcularIMC(peso, altura):
    try:
        return round(peso / (altura ** 2), 2)
    except ZeroDivisionError:
        return 0

def registrarPersona(lista):
    borrarPantalla()
    print("\n::: Registrar nueva persona :::\n")
    nombre = input("Nombre: ").strip().title()
    edad = int(input("Edad: "))
    peso = float(input("Peso (kg): "))
    altura = float(input("Altura (m): "))
    imc = calcularIMC(peso, altura)

    persona = {
        "nombre": nombre,
        "edad": edad,
        "peso": peso,
        "altura": altura,
        "imc": imc
    }

    lista.append(persona)
    print("\n✅ Registro exitoso!")

def mostrarPersonas(lista):
    borrarPantalla()
    print("\n::: Lista de personas registradas :::\n")
    if not lista:
        print("No hay registros.")
    else:
        for i, persona in enumerate(lista, start=1):
            print(f"{i}. {persona['nombre']} | Edad: {persona['edad']} | Peso: {persona['peso']}kg | Altura: {persona['altura']}m | IMC: {persona['imc']}")

def buscarPersona(lista):
    borrarPantalla()
    nombre = input("Ingresa el nombre a buscar: ").strip().title()
    encontrados = [p for p in lista if p['nombre'] == nombre]

    if encontrados:
        for p in encontrados:
            print(f"\n🔍 {p['nombre']} - Edad: {p['edad']} - Peso: {p['peso']}kg - Altura: {p['altura']}m - IMC: {p['imc']}")
    else:
        print("\n❌ Persona no encontrada.")

def modificarPersona(lista):
    borrarPantalla()
    nombre = input("Nombre de la persona a modificar: ").strip().title()
    for persona in lista:
        if persona['nombre'] == nombre:
            print("\nDatos actuales:")
            print(persona)
            persona['edad'] = int(input("Nueva edad: "))
            persona['peso'] = float(input("Nuevo peso (kg): "))
            persona['altura'] = float(input("Nueva altura (m): "))
            persona['imc'] = calcularIMC(persona['peso'], persona['altura'])
            print("\n✅ Modificación exitosa.")
            return
    print("❌ No se encontró esa persona.")

def eliminarPersona(lista):
    borrarPantalla()
    nombre = input("Nombre de la persona a eliminar: ").strip().title()
    for persona in lista:
        if persona['nombre'] == nombre:
            lista.remove(persona)
            print("🗑️ Persona eliminada con éxito.")
            return
    print("❌ Persona no encontrada.")

def limpiarRegistros(lista):
    borrarPantalla()
    confirm = input("¿Estás seguro de borrar todos los registros? (si/no): ").lower()
    if confirm == "si":
        lista.clear()
        print("✅ Todos los registros fueron eliminados.")

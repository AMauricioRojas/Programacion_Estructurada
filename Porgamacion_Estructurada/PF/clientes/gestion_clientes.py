import os
import mysql.connector
from tabulate import tabulate
from db.conexion import crear_conexion
from openpyxl import Workbook

def borrar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def agregar_cliente():
    borrar_pantalla()
    print("📝 REGISTRO DE CLIENTE")
    nombre = input("👤 Nombre: ")
    edad = input("🎂 Edad: ")
    peso = input("⚖️ Peso (kg): ")
    estatura = input("📏 Estatura (m): ")
    objetivo = input("🎯 Objetivo (subir, bajar, tonificar): ")

    try:
        conexion = crear_conexion()
        if conexion:
            cursor = conexion.cursor()
            consulta = "INSERT INTO clientes (nombre, edad, peso, estatura, objetivo) VALUES (%s, %s, %s, %s, %s)"
            valores = (nombre, edad, peso, estatura, objetivo)
            cursor.execute(consulta, valores)
            conexion.commit()
            print("✅ Cliente registrado correctamente.")
    except mysql.connector.Error as e:
        print("❌ Error al agregar cliente:", e)
    finally:
        if conexion.is_connected():
            conexion.close()
    input("⏸️ Presiona Enter para continuar...")

def listar_clientes():
    borrar_pantalla()
    print("📋 LISTA DE CLIENTES")
    try:
        conexion = crear_conexion()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM clientes")
            clientes = cursor.fetchall()

            if clientes:
                print(tabulate(clientes, headers=["ID", "Nombre", "Edad", "Peso", "Estatura", "Objetivo"], tablefmt="fancy_grid"))
            else:
                print("📭 No hay clientes registrados.")
    except mysql.connector.Error as e:
        print("❌ Error al obtener la lista de clientes:", e)
    finally:
        if conexion.is_connected():
            conexion.close()
    input("⏸️ Presiona Enter para continuar...")

def editar_cliente():
    borrar_pantalla()
    print("✏️ EDITAR CLIENTE")
    id_cliente = input("🔢 Ingresa el ID del cliente a editar: ")

    try:
        conexion = crear_conexion()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM clientes WHERE id = %s", (id_cliente,))
            cliente = cursor.fetchone()

            if cliente:
                print("\n📌 Datos actuales:")
                print(f"Nombre: {cliente[1]}")
                print(f"Edad: {cliente[2]}")
                print(f"Peso: {cliente[3]}")
                print(f"Estatura: {cliente[4]}")
                print(f"Objetivo: {cliente[5]}")

                nombre = input("📝 Nuevo nombre (dejar en blanco para no cambiar): ") or cliente[1]
                edad = input("📝 Nueva edad: ") or cliente[2]
                peso = input("📝 Nuevo peso: ") or cliente[3]
                estatura = input("📝 Nueva estatura: ") or cliente[4]
                objetivo = input("📝 Nuevo objetivo: ") or cliente[5]

                consulta = """
                    UPDATE clientes SET nombre=%s, edad=%s, peso=%s, estatura=%s, objetivo=%s
                    WHERE id=%s
                """
                cursor.execute(consulta, (nombre, edad, peso, estatura, objetivo, id_cliente))
                conexion.commit()
                print("✅ Cliente actualizado correctamente.")
            else:
                print("❌ No se encontró un cliente con ese ID.")
    except mysql.connector.Error as e:
        print("❌ Error al editar cliente:", e)
    finally:
        if conexion.is_connected():
            conexion.close()
    input("⏸️ Presiona Enter para continuar...")

def eliminar_cliente():
    borrar_pantalla()
    print("🗑️ ELIMINAR CLIENTE")
    id_cliente = input("❗ Ingresa el ID del cliente a eliminar: ")

    try:
        conexion = crear_conexion()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM clientes WHERE id = %s", (id_cliente,))
            cliente = cursor.fetchone()

            if cliente:
                confirmar = input(f"⚠️ ¿Estás seguro de eliminar al cliente {cliente[1]}? (s/n): ").lower()
                if confirmar == "s":
                    cursor.execute("DELETE FROM clientes WHERE id = %s", (id_cliente,))
                    conexion.commit()
                    print("✅ Cliente eliminado correctamente.")
                else:
                    print("🔁 Operación cancelada.")
            else:
                print("❌ No se encontró un cliente con ese ID.")
    except mysql.connector.Error as e:
        print("❌ Error al eliminar cliente:", e)
    finally:
        if conexion.is_connected():
            conexion.close()
    input("⏸️ Presiona Enter para continuar...")

def exportar_clientes_a_excel():
    try:
        conexion = crear_conexion()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM clientes")
            clientes = cursor.fetchall()

            libro = Workbook()
            hoja = libro.active
            hoja.title = "Clientes"

            encabezados = ["ID", "Nombre", "Edad", "Peso", "Estatura", "Objetivo"]
            hoja.append(encabezados)

            for cliente in clientes:
                hoja.append(cliente)

            ruta_archivo = os.path.join(os.getcwd(), "clientes.xlsx")
            libro.save(ruta_archivo)

            print(f"\n✅ Exportado como 'clientes.xlsx' en:\n{ruta_archivo}\n")

    except mysql.connector.Error as e:
        print("❌ Error al exportar los datos:", e)
    finally:
        if conexion.is_connected():
            conexion.close()
    input("⏸️ Presiona Enter para continuar...")

def menu_clientes():
    while True:
        borrar_pantalla()
        print("📁 MENÚ DE CLIENTES")
        print("1. ➕ Agregar cliente")
        print("2. 📄 Listar clientes")
        print("3. ✏️ Editar cliente")
        print("4. 🗑️ Eliminar cliente")
        print("5. 📤 Exportar clientes a Excel")
        print("6. 🔙 Regresar al menú principal")

        opcion = input("\n👉 Elige una opción: ")

        if opcion == "1":
            agregar_cliente()
        elif opcion == "2":
            listar_clientes()
        elif opcion == "3":
            editar_cliente()
        elif opcion == "4":
            eliminar_cliente()
        elif opcion == "5":
            exportar_clientes_a_excel()
        elif opcion == "6":
            break
        else:
            print("❌ Opción inválida, intenta de nuevo.")
            input("⏸️ Presiona Enter para continuar...")

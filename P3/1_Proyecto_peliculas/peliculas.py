import mysql.connector
from mysql.connector import Error
import os

pelicula = {}

def borrarPantalla():
    os.system("cls" if os.name == "nt" else "clear")

def esperarTecla():
    input("\n⏸️ Oprime cualquier tecla para continuar...")

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bd_peliculas"
        )
        return conexion
    except Error as e:
        print(f"❌ Error de conexión que se presento es: {e}")
        return None

def crearPeliculas():
    conexionBD = conectar()
    if conexionBD is not None:
        borrarPantalla()
        print("🆕 .:: Alta de Película ::.\n")

        pelicula["nombre"] = input("🎬 Nombre: ").upper().strip()
        pelicula["categoria"] = input("🏷️ Categoría: ").upper().strip()
        pelicula["clasificacion"] = input("🔞 Clasificación: ").upper().strip()
        pelicula["genero"] = input("🎭 Género: ").upper().strip()
        pelicula["idioma"] = input("🗣️ Idioma: ").upper().strip()

        try:
            cursor = conexionBD.cursor()
            sql = "INSERT INTO peliculas (nombre, categoria, clasificacion, genero, idioma) VALUES (%s, %s, %s, %s, %s)"
            valores = (pelicula["nombre"], pelicula["categoria"], pelicula["clasificacion"], pelicula["genero"], pelicula["idioma"])
            cursor.execute(sql, valores)
            conexionBD.commit()
            print("\n✅ ¡Película registrada con éxito!")
        except Error as e:
            print(f"❌ Error al insertar película: {e}")
        conexionBD.close()

def mostrarPeliculas():
    borrarPantalla()
    conexionBD = conectar()
    if conexionBD is not None:
        print("\n📋 .:: Lista de Películas ::.\n")
        cursor = conexionBD.cursor()
        sql="SELECT * FROM peliculas"
        cursor.execute(sql)
        registros = cursor.fetchall()

        if registros:
            print(f"{'ID':<10} {'🎬 Nombre':<15} {'🏷️ Categoría':<15} {'🔞 Clasificación':<15} {'🎭 Género':<15} {'🗣️ Idioma':<15}")
            print("-" * 90)
            for peli in registros:
                print(f"{peli[0]:<10} {peli[1]:<15} {peli[2]:<15} {peli[3]:<15} {peli[4]:<15} {peli[5]:<15}")
        else:
            print("⚠️ No hay películas registradas.")
        conexionBD.close()

def buscarPeliculas():
    borrarPantalla()
    conexionBD = conectar()
    if conexionBD is not None:
        print("\n🔍 .:: Buscar Película ::.\n")
        nombre = input("Ingresa el nombre de la película: ").upper().strip()
        cursor = conexionBD.cursor()
        cursor.execute("SELECT * FROM peliculas WHERE nombre = %s", (nombre,))
        resultados = cursor.fetchall()

        if resultados:
            print(f"{'ID':<5} {'🎬 Nombre':<20} {'🏷️ Categoría':<15} {'🔞 Clasificación':<15} {'🎭 Género':<15} {'🗣️ Idioma':<15}")
            print("-" * 90)
            for peli in resultados:
                print(f"{peli[0]:<5} {peli[1]:<20} {peli[2]:<15} {peli[3]:<15} {peli[4]:<15} {peli[5]:<15}")
        else:
            print("⚠️ No se encontró ninguna película con ese nombre.")
        conexionBD.close()

def borrarPeliculas():
    borrarPantalla()
    conexionBD = conectar()
    if conexionBD is not None:
        print("\n🗑️ .:: Borrar Película ::.\n")
        nombre = input("Ingresa el nombre de la película a borrar: ").upper().strip()
        cursor = conexionBD.cursor()
        cursor.execute("SELECT * FROM peliculas WHERE nombre = %s", (nombre,))
        registros = cursor.fetchall()

        if registros:
            print(f"{'ID':<5} {'🎬 Nombre':<20} {'🏷️ Categoría':<15} {'🔞 Clasificación':<15} {'🎭 Género':<15} {'🗣️ Idioma':<15}")
            print("-" * 90)
            for peli in registros:
                print(f"{peli[0]:<5} {peli[1]:<20} {peli[2]:<15} {peli[3]:<15} {peli[4]:<15} {peli[5]:<15}")
            confirmacion = input(f"\n¿Deseas borrar la película '{nombre}'? (si/no): ").lower().strp()
            if confirmacion == "si":
                cursor.execute("DELETE FROM peliculas WHERE nombre = %s", (nombre,))
                conexionBD.commit()
                print("✅ Película eliminada con éxito.")
        else:
            print("⚠️ No se encontró la película.")
        conexionBD.close()

def modificarCaracteristicaPeliculas():
    borrarPantalla()
    conexionBD = conectar()
    if conexionBD is not None:
        print("\n🛠️ .:: Modificar Película ::.\n")
        nombre_original = input("Ingresa el nombre de la película a modificar: ").upper().strip()

        cursor = conexionBD.cursor()
        cursor.execute("SELECT * FROM peliculas WHERE nombre = %s", (nombre_original,))
        registro = cursor.fetchone()

        if registro:
            # Cargar los datos actuales al diccionario
            pelicula["id"] = registro[0]
            pelicula["nombre"] = registro[1]
            pelicula["categoria"] = registro[2]
            pelicula["clasificacion"] = registro[3]
            pelicula["genero"] = registro[4]
            pelicula["idioma"] = registro[5]

            print("\n🎬 Película encontrada:")
            print(f"{'ID':<5} {'🎬 Nombre':<20} {'🏷️ Categoría':<15} {'🔞 Clasificación':<15} {'🎭 Género':<15} {'🗣️ Idioma':<15}")
            print("-" * 90)
            print(f"{pelicula['id']:<5} {pelicula['nombre']:<20} {pelicula['categoria']:<15} {pelicula['clasificacion']:<15} {pelicula['genero']:<15} {pelicula['idioma']:<15}")

            print("\n✏️ Ingresa los nuevos valores (deja en blanco para mantener los actuales):")

            nuevo_nombre = input("Nuevo nombre: ").upper().strip()
            nueva_categoria = input("Nueva categoría: ").upper().strip()
            nueva_clasificacion = input("Nueva clasificación: ").upper().strip()
            nuevo_genero = input("Nuevo género: ").upper().strip()
            nuevo_idioma = input("Nuevo idioma: ").upper().strip()

            # Solo se actualiza si el usuario escribió algo
            if nuevo_nombre:
                pelicula["nombre"] = nuevo_nombre
            if nueva_categoria:
                pelicula["categoria"] = nueva_categoria
            if nueva_clasificacion:
                pelicula["clasificacion"] = nueva_clasificacion
            if nuevo_genero:
                pelicula["genero"] = nuevo_genero
            if nuevo_idioma:
                pelicula["idioma"] = nuevo_idioma

            # Hacer el UPDATE en la base de datos usando los valores del diccionario
            sql = """
                UPDATE peliculas
                SET nombre = %s, categoria = %s, clasificacion = %s, genero = %s, idioma = %s
                WHERE id = %s
            """
            valores = (
                pelicula["nombre"],
                pelicula["categoria"],
                pelicula["clasificacion"],
                pelicula["genero"],
                pelicula["idioma"],
                pelicula["id"]
            )
            cursor.execute(sql, valores)
            conexionBD.commit()

            print("\n✅ ¡Película modificada con éxito!")
        else:
            print("⚠️ No se encontró la película.")
        conexionBD.close()
        esperarTecla()


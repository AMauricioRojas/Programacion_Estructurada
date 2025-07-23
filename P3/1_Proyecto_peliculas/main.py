'''
Crear un proyecto que permita gestionar (administrar) peliculas, colocar un menú de opciones para agregar, eliminar, modificar y consultar peliculas

NOTAS: 
1.- Utilizar funciones y mandar llamar desde otro archivo
2.- Utilizar diccionarios para almacenar los siguientes atributos: (nombre, categoria, clasificación, género, idioma) de las peliculas.
3.- Utilizar e implementar una BD para gestionar las peliculas
'''



import peliculas

opcion = True
while opcion:
    peliculas.borrarPantalla()
    print("\n🎬\t\t..::: CINEPOLIS CLON :::... ")
    print("📽️\t\t..::: Sistema de Gestión de Películas :::..\n")
    print("1️⃣  Crear Película")
    print("2️⃣  Borrar Película")
    print("3️⃣  Mostrar Películas")
    print("4️⃣  Modificar Características")
    print("5️⃣  Buscar Película")
    print("6️⃣  SALIR")

    opcion = input("\n📝 Elige una opción: ").upper()

    match opcion:
        case "1":
            peliculas.crearPeliculas()
            peliculas.esperarTecla()
        case "2":
            peliculas.borrarPeliculas()
            peliculas.esperarTecla()
        case "3":
            peliculas.mostrarPeliculas()
            peliculas.esperarTecla()
        case "4":
            peliculas.modificarCaracteristicaPeliculas()
            peliculas.esperarTecla()
        case "5":
            peliculas.buscarPeliculas()
            peliculas.esperarTecla()
        case "6":
            opcion = False
            peliculas.borrarPantalla()
            print("\n👋 Terminaste la ejecución del sistema. ¡Hasta luego!")
        case _:
            input("\n❌ Opción inválida. Inténtalo nuevamente...")

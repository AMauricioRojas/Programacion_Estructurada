import peliculas

opcion=True
while opcion:
    peliculas.borrarPantalla()
    print("\n\t..::: CINEPOLIS CLON :::... \n..::: Sistema de Gestión de Peliculas :::...\n\n 1.- Agregar  \n 2.- Borrar \n 3.- Modificar \n 4.- Mostrar \n 5.- Buscar \n 6.- Limpiar \n 7.- SALIR ")
    opcion=input("\t\n Elige una opción: ").upper()

    match opcion:
        case "1":
            peliculas.agregarPeliculas()
            peliculas.esperarTecla()
        case "2":
            print(".:: Eliminar Peliculas ::.") 
            input("Oprima cualquier tecla para continuar ...") 
        case "3":
            print(".:: Modificar Peliculas ::.") 
            input("Oprima cualquier tecla para continuar ...")    
        case "4":
            peliculas.consultarPeliculas() 
            peliculas.esperarTecla()
        case "5": 
            peliculas.buscarPeliculas()
            peliculas.esperarTecla()
        case "6": 
            peliculas.vaciarPeliculas()
            peliculas.esperarTecla()
        case "7":
            opcion=False    
            print("Terminaste la ejecucion del SW")
        case _: 
            input("Opción invalida vuelva a intentarlo ... por favor")
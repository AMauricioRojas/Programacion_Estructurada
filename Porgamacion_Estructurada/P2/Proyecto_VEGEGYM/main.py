import gimnasio

def main():
    opcion = True
    personas = []

    while opcion:
        gimnasio.borrarPantalla()
        print("\n\t..::: GYM TRACKER SYSTEM :::..\n")
        print(" 1.- Registrar persona")
        print(" 2.- Mostrar registros")
        print(" 3.- Buscar persona")
        print(" 4.- Modificar persona")
        print(" 5.- Eliminar persona")
        print(" 6.- Limpiar todos los registros")
        print(" 7.- Salir")

        op = input("\nSelecciona una opción: ").strip()

        match op:
            case "1":
                gimnasio.registrarPersona(personas)
                gimnasio.esperarTecla()
            case "2":
                gimnasio.mostrarPersonas(personas)
                gimnasio.esperarTecla()
            case "3":
                gimnasio.buscarPersona(personas)
                gimnasio.esperarTecla()
            case "4":
                gimnasio.modificarPersona(personas)
                gimnasio.esperarTecla()
            case "5":
                gimnasio.eliminarPersona(personas)
                gimnasio.esperarTecla()
            case "6":
                gimnasio.limpiarRegistros(personas)
                gimnasio.esperarTecla()
            case "7":
                opcion = False
                print("\nGracias por usar el sistema del gimnasio.")
            case _:
                input("Opción inválida. Presiona Enter para continuar...")

if __name__ == "__main__":
    main()


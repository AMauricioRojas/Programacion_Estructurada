import agenda

def main():
    agenda_contactos = {}  # Diccionario para almacenar contactos (nombre: [tel, email])
    
    while True:
        agenda.borrarPantalla()
        opcion = agenda.menu_principal()

        match opcion:
            case "1":  # Agregar contacto
                agenda.agregar_contacto(agenda_contactos)
                agenda.esperarTecla()
            case "2":  # Mostrar contactos
                agenda.mostrar_contacto(agenda_contactos)
                agenda.esperarTecla() 
            case "3":  # Buscar contacto
                agenda.buscar_contacto(agenda_contactos)
                agenda.esperarTecla()   
            case "4":  # Modificar contacto (nueva posición)
                agenda.modificar_contacto(agenda_contactos)
                agenda.esperarTecla()
            case "5":  # Salir (ahora es opción 5)
                agenda.borrarPantalla()
                print("✅ Programa terminado. ¡Hasta pronto!")
                break
            case _:
                print("❌ Opción inválida. Inténtalo de nuevo.")
                agenda.esperarTecla()

if __name__ == "__main__":
    main()

#crar un menu de opciones que permita gestionar(administrar) calificaciones colocar un menu de opciones para agregar,mostrar y calcular promedios de las calificaciones
#notas 
#1 utilizar funciones y mandar llaar desde otro archio
#2 Utilizar listas para almacenar el nombre de un alumno y 3 calificaciones 

import calificaciones

def main():
        opcion = True
        datos=[]

        while opcion:
            calificaciones.borrarPantalla()
            opcion=calificaciones.menu_principal()
            
            match opcion:
                case "1":
                    calificaciones.agregar_Calificaciones(datos)
                    calificaciones.esperarTecla()
                case "2":
                    calificaciones.mostrar_Calificaciones(datos)
                    calificaciones.esperarTecla()
                case "3":
                    calificaciones.calcular_Promedios(datos)
                    calificaciones.esperarTecla()
                case "4":
                    opcion = False
                    calificaciones.borrarPantalla()
                    print("\n\tTerminaste la ejecución del SW")
                case _:
                    input("\n\tOpción inválida, vuelva a intentarlo... por favor")

if __name__=="__main__":
    main()

"""" case "5":
            calificaciones.modificarCaracteristicaPeliculas()
            calificaciones.esperarTecla()
        case "6":
            calificaciones.borrarCaracteristicaPeliculas()
            calificaciones.esperarTecla()
        case "7":
            opcion = False
            calificaciones.borrarPantalla()"""

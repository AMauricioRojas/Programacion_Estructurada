
#lista=[
    #["ruben",10.0,10.0,10.0],
    #["Diana",10.0,9.8,8.0],
    #["Jose",5.0,6.0,7.0]
#]

def borrarPantalla():
    import os 
    os.system("cls")

def esperarTecla():
    print("\n\t\t...Oprima una tecla para continuar...")
    input()

def agregar_Calificaciones(lista): 
    nombre = input("Ingresa el nombre del alumno: ").strip()
    try:
        cal1 = float(input("Ingresa la calificación 1: "))
        cal2 = float(input("Ingresa la calificación 2: "))
        cal3 = float(input("Ingresa la calificación 3: "))
        lista.append([nombre, cal1, cal2, cal3])
        print(f"\n✅ Alumno '{nombre}' agregado correctamente.")
    except ValueError:
        print("\n❌ Error: Ingresa solo números válidos para las calificaciones.")

def menu_principal():

    print("\n\t..::: Sistema de Gestion de Calificaciones:::..\n 1.- Agregar \n 2.- Mostrar \n 3.- Calcular promedio de lascalificaciones\n 4.- Salir")
    #\n 4.- Agregar Característica \n 5.- Modificar Característica \n 6.- Borrar Característica \n 7.- SALIR ")
    opcion = input("\t\n Elige una opción(1-4): ").upper()
    return opcion

def mostrar_Calificaciones(lista):
    if not lista:
        print("\n⚠️ No hay alumnos registrados.")
        return
    print("\n📋 Lista de alumnos y sus calificaciones:")
    for alumno in lista:
        print(f" - {alumno[0]}: {alumno[1]}, {alumno[2]}, {alumno[3]}")

def calcular_Promedios(lista):
    if not lista:
        print("\n⚠️ No hay alumnos registrados.")
        return
    print("\n📊 Promedios de los alumnos:")
    for alumno in lista:
        promedio = (alumno[1] + alumno[2] + alumno[3]) / 3
        print(f" - {alumno[0]}: {promedio:.2f}")
#agregar,mostrar y calcular promedio
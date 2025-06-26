pelicula = {}

def borrarPantalla():
    import os 
    os.system("cls")

def esperarTecla():
    print("\n\t\t...Oprima una tecla para continuar...")
    input()

def crearPeliculas():

    borrarPantalla()
    print("\n\t::: Alta de Películas :::\n")
    #pelicula["nombre"]=input("Ingresa el nombre de la película: ").upper().strip()
    pelicula.update({"nombre": input("Ingresa el nombre: ")})
    pelicula.update({"categoria": input("Ingresa la categoría: ")})
    pelicula.update({"clasificacion": input("Ingresa la clasificación: ")})
    pelicula.update({"genero": input("Ingresa el género: ")})
    pelicula.update({"idioma": input("Ingresa el idioma: ")})
    
    input("\n\t::: LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::")

def mostrarPeliculas():
    borrarPantalla()
    print("\n\t:::Consultar o Mostrar la Pelicula:::\n")
    if len(pelicula) > 0:
        for i in pelicula:
            print(f"\t{i} : {pelicula[i]}")
    else:
        print("\t::: No hay peliculas en el sistema :::")

def vaciarPeliculas():
    borrarPantalla()
    print("\n\t.::Vaciar o quitar todas las peliculas::.")
    resp = input("¿Deseas borrar TODAS las peliculas del sistema?(Si\\No)").lower().strip()

    if resp == "si":
        pelicula.clear()
        print("\n\t\t::: LA OPERACION SE REALIZO CON EXITO:::")

def agregarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t::: Agregar Característica a Películas :::\n")
    atributo = input("Ingresa la nueva característica de la película: ").lower().strip()
    valor = input("Ingresa el valor de la característica de la película: ").strip()
    
    pelicula[atributo] = valor
    print("\n\t\t::: LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::")

def borrarPeliculas():
    borrarPantalla()
    print("\n\t::: Borrar o Quitar TODAS las Películas :::\n")
    resp = input("¿Deseas quitar o borrar todas las películas del sistema? (Si/No): ").lower()
    
    if resp == "si":
        pelicula.clear()
        input("\n\t\t::: LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::")

def modificarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t::: Modificar Característica de Película :::\n")
    if len(pelicula) == 0:
        print("\t::: No hay películas en el sistema :::")
        return
    
    print("\nCaracterísticas disponibles:")
    for key in pelicula.keys():
        print(f"- {key}")
    
    atributo = input("\nIngresa la característica a modificar: ").lower().strip()
    
    if atributo in pelicula:
        nuevo_valor = input(f"Ingresa el nuevo valor para '{atributo}': ").strip()
        pelicula[atributo] = nuevo_valor
        print("\n\t\t::: LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::")
    else:
        print("\n\t::: La característica ingresada no existe :::")

def modificarCaracteristicaPelicula():
    borrarPantalla()
    print("\n\t.:: Modificar Características a Películas  ::. \n")
    if len(pelicula) > 0:
        print(f"\n\tValor actuales: \n ")
        for i in pelicula:
            print(f"\t{(i)} : {pelicula[i]}")
            resp = input(f"\t¿Deseas cambiar el valor de {i}? (Si/No) ")
            if resp == "si":
                pelicula.update({f"{i}": input("\t↻ el nuevo valor: ").upper().strip()})
                print("\n\t\t ::: ¡LA OPERACION SE REALIZO CON EXÍTO!  :::") 
    else:
        print("\t..:: No hay peliculas en Sistema  ::..")
        esperarTecla()

def borrarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t::: Borrar Característica de Película :::\n")
    if len(pelicula) == 0:
        print("\t::: No hay películas en el sistema :::")
        return
    
    print("\nCaracterísticas disponibles:")
    for key in pelicula.keys():
        print(f"- {key}")
    resp = input("\n¿Deseas eliminar una característica? (Si/No): ").lower().strip()
    if resp != "si":
        print("\n\t::: Operación cancelada :::")
    else:
        atributo = input("\nIngresa la característica a eliminar: ").lower().strip()
        
        if atributo in pelicula:
            del pelicula[atributo]
            print("\n\t\t::: LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::")
        else:
            print("\n\t::: La característica ingresada no existe :::")

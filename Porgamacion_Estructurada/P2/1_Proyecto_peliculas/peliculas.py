peliculas=[]
def borrarPantalla():
    import os 
    os.system ("cls")

def esperarTecla():
    print("\n\t\t...Oprima una tecla para continuar...")
    input()

def agregarPeliculas():
    borrarPantalla()
    print("\n\t.:: Agregar Peliculas::.")
    peliculas.append(input("Ingrese el nombre:" ).upper().strip())
    print("\n\t\t::: LA OPERACION SE REALIZO CON EXITO:::")

def consultarPeliculas():
    borrarPantalla()
    print("\n\t.:: Consultar o mostrar Películas ::.")
    if len(peliculas) > 0:
        for i in range(len(peliculas)):
            print(f"\t {i+1}: {peliculas[i]}")
    else:
        print("\n\tNo hay películas registradas en el sistema.")


def vaciarPeliculas():
    borrarPantalla()
    print("\n\t.::Vaciar o quitar todas las peliculas::.")
    resp = input("¿Deseas borrar TODAS las peliculas del sistema?(Si\\No)").lower().strip()

    if resp=="si":
        peliculas.clear()
        print("\n\t\t::: LA OPERACION SE REALIZO CON EXITO:::")

def buscarPeliculas():
    borrarPantalla()
    print("\n\t.::Buscar peliculas::.\n")
    peliculas_buscar=input("Ingrese el nombre de la pelicula a buscar:").upper().strip()
    encontro=0
    if not (peliculas_buscar in peliculas):
        print("\n\t\t¡ NO se encontro la pelicula")
    else:
        for i in range(0,len(peliculas)):
            if peliculas_buscar==peliculas[i]:
                print(f"\nLa pelicula {peliculas_buscar} si la tenemos y esta en la casilla :{i+1}")
                encontro+=1
        print("\nTenemos{encontro} pelicula(s) con este titulo ")
        print("\n\t\t::: LA OPERACION SE REALIZO CON EXITO:::")


def eliminarPeliculas():
    borrarPantalla()
    print("\n\t.::Borrar peliculas::.\n")
    peliculas_buscar=input("Ingrese el nombre de la pelicula a borrar:").upper().strip()
    encontro=0
    if not (peliculas_buscar in peliculas):
        print("\n\t\t¡ NO se encontro la pelicula")
    else:
        resp="si"
        while peliculas_buscar in peliculas and resp=="si":
            resp=input("¿Deseas borrar la pelicula del sistema(Si/No)")
            if resp=="si":
                posicion=peliculas.index(peliculas_buscar)
                print(f"\nLa pelicula que se borro es {peliculas_buscar} y estaba en la casilla :{posicion+1}")
                peliculas.remove(peliculas_buscar)
                encontro+=1
                print("\n\t\t::: LA OPERACION SE REALIZO CON EXITO:::")
                print(f"\n\t se borro {encontro} pelicula(s) con este titulo")
#ejemplo 1 crear una lista de numeros e imprimir el contenido
import os
os.system("cls")
numeros=[12,14,12,16,19,20,22]
print(numeros)

#2 forma trabja con eel valor
for i in numeros:
    print(i)

#3 forma trabaja con los indices
for i in range (0,len(numeros)):
    print(numeros[i])

#Ejemplo2 crear una lista de palabras y posteriormente buscar la coincidencia de una palabra
os.system("cls")
palabras=["Hola","Adios","Eda","Hermano","lista","lista","suko"]
print(palabras)
"""print(palabras.count("lista"))"""

palabra_buscar=input("dame la palabra a buscar")

if palabra_buscar in palabras:
    print("Se encontro la palabra ")
else:
    print("No se encontro la palabra ")

"""palabras2=["","","","",""]
palabras2[0]="casa"
palabras2[2]="casa"
palabras2[3]="hola"
print(palabras2)"""

#2 forma
Encontro=False
for i in palabras:
    if i==palabra_buscar:
        print("Se encontro la palabra ")
        Encontro=True

if Encontro:
    print("se encontro la palabra")
else:
    print("No se encontro la palabra ")



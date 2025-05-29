"""List(Array)
SOn colleciones o conjuntos de datos/valores bajo un mismo nomnre,para acceder a los valores se hace como un indice numerico

NOTA: sus valores si son modificables 

La lista es una coleccion ordenada y modificable. Permite miembros duplicados 
"""
import os 
os.system("cls")

#FUNCIONES MAS COMUNES EN LAS LISTAS
paises=["Mexico","Brasil","España","Canada"]

numeros=[23,12,100,34]

varios=["Hola",True,33,3.12]

#ordenar las listas

print(numeros)
print(paises)
print(varios)

numeros.sort()
print(numeros)

paises.sort()
print(paises)

#agregar o insertar o añadir un elemento a la lista
#1 forma paises=["Mexico","Brasil","España","Canada"]
print(paises)
paises.append("Honduras")
print(paises)

#2 forma paises=["Mexico","Brasil","España","Canada"]
paises.insert(1,"Honduras")
print(paises)

#Eliminar o borrar o suprimir o quitar un elemento de la lista
#1 forma paises=["Mexico","Brasil","España","Canada"]
paises.sort()
print(paises)

paises.pop(4)
print(paises)

#2 forma paises=["Mexico","Brasil","España","Canada"]
paises.remove("Honduras")
print(paises)

#buscar un elemento dentro de la lista

print("Brasil" in paises)

#contar el numero de veces que un elemento existe o esta dentro de una lista
#numeros=[23,12,100,34]
print(numeros)
print(numeros.count(12))
numeros.insert(1,12)
print(numeros)
print(numeros.count(101))

#Dar la vuelta a los elementos de una lista
print(paises)
print(numeros)
paises.reverse()
numeros.reverse()
print(paises)
print(numeros)

#conocer el indice o la posicion de un dato o valor de la lista
print(paises.index("España"))

#posicion=paises.index("España")

#paises[posicion]="ESPAÑA"
#print(paises)

#Unir el contenido de dos o mas listas
#Numeros=[100,34,23,12,12]

numeros2=[300,500,100]
print(numeros)
print(numeros2)

numeros.extend(numeros2)
print(numeros)

paises.extend(numeros2)
print(paises)







import os
os.system("cls")

print("Sistema para calificaciones")

calificaciones=[]

num=int(input("¿Cuantas calificaciones deseas ingresar? "))

for i in range(num):
    nota= float(input(f"Ingresa la alificacion{i+1} "))
    calificaciones.append(nota)

print("\nTus calificaciones son: ")
print(calificaciones)

promedio=sum(calificaciones) / len(calificaciones)
print(f"\nEl prom,edio es: {promedio:.2f} ")


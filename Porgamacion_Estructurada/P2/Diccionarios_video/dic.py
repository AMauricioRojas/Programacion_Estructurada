import os 
os.system("cls")

print("Sistema de registro de productos")
productos={

}

num=int(input("¿Cuantos productos vas a registrar? "))

for i in range (num):
    nombre=input(f"Nombre del producto{i+1} :")
    precio= float(input("Precio: "))
    productos[nombre]=precio

print("LISTA DE PRODUCTOS Y PRECIOS")
for nombre,precio in productos.items():
    print(f"{nombre}:${precio:.2f}")

buscar= input("Nombre del producto a buscar")
if buscar in productos:
    print(f"✅El precio de {buscar} es $ {productos[buscar]:.2f}")
else:
    print("El producto no se encuentra")

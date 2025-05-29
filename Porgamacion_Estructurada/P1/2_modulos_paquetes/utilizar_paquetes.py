from paquete1 import modulos

print(modulos.saludar("Daniel Contreras Ruano"))

modulos.borrarPantalla()
nom,tel=modulos.solicitarDatos2()
print(f"\n\t.:: Agenda telefonica::.\n\tNombre: {nom}\n\tTelefono: {tel}")
modulos.espereTecla()
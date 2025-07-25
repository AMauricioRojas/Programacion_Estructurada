import funciones
from usuarios import usuario
from notas import nota
import getpass
from conexionBD import conexion, cursor  # Importamos la conexión y cursor

def main():
    opcion = True
    while opcion:
        funciones.borrarPantalla()
        opcion = funciones.menu_usurios()

        if opcion == "1" or opcion == "REGISTRO":
            funciones.borrarPantalla()
            print("\n \t ..:: Registro en el Sistema ::..")
            nombre = input("\t ¿Cuál es tu nombre?: ").upper().strip()
            apellidos = input("\t ¿Cuáles son tus apellidos?: ").upper().strip()
            email = input("\t Ingresa tu email: ").lower().strip()
            password = getpass.getpass("\t Ingresa tu contraseña: ").strip()

            registro = usuario.registrar(nombre, apellidos, email, password)
            if registro:
                print(f"\n\t{nombre} {apellidos} se registró correctamente con el email {email}")
            else:
                print("\n\tNo fue posible registrar al usuario, inténtalo más tarde")

            funciones.esperarTecla()
            
        elif opcion == "2" or opcion == "LOGIN": 
            funciones.borrarPantalla()
            print("\n \t ..:: Inicio de Sesión ::..")     
            email = input("\t Ingresa tu E-mail: ").lower().strip()
            password = getpass.getpass("\t Ingresa tu contraseña: ").strip()
            
            lista_usuario = usuario.inicio_sesion(email, password)
            if lista_usuario:
                menu_notas(lista_usuario[0], lista_usuario[1], lista_usuario[2])
            else:
                print("\n\tEmail y/o contraseña incorrectos, por favor verifica y vuelve a intentar")
                funciones.esperarTecla()
              
        elif opcion == "3" or opcion == "SALIR": 
            print("\n\tTerminó la Ejecución del Sistema")
            # Cerramos la conexión a la base de datos al salir
            if conexion.is_connected():
                cursor.close()
                conexion.close()
            opcion = False
            funciones.esperarTecla()  
        else:
            print("\n\tOpción no válida")
            funciones.esperarTecla() 

def menu_notas(usuario_id, nombre, apellidos):
    while True:
        funciones.borrarPantalla()
        print(f"\n \t \t \t Bienvenido {nombre} {apellidos}, has iniciado sesión ...")
        opcion = funciones.menu_notas()

        if opcion == '1' or opcion == "CREAR":
            funciones.borrarPantalla()
            print(f"\n \t .:: Crear Nota ::. ")
            titulo = input("\tTítulo: ")
            descripcion = input("\tDescripción: ")
            
            resultado = nota.crear(usuario_id, titulo, descripcion)
            if resultado:
                print(f"\n\t✅ Se creó satisfactoriamente la nota: {titulo}")
            else:
                print("\n\t❌ No fue posible crear la nota en este momento, por favor intentar más tarde")
            funciones.esperarTecla()    
            
        elif opcion == '2' or opcion == "MOSTRAR":
            funciones.borrarPantalla()
            print(f"\n \t .:: Notas de {nombre} {apellidos} ::. \n")
            notas = nota.mostrar(usuario_id)
            
            if notas:
                print(f"{'🔢 ID':<6} {'📌 TÍTULO':<30} {'📝 DESCRIPCIÓN':<40} {'📅 FECHA':<12}")
                print("═" * 90)
                for n in notas:
                    desc_corta = (n[2][:37] + '...') if len(n[2]) > 40 else n[2]
                    fecha_formateada = n[3].strftime('%d/%m/%Y') if n[3] else 'N/A'
                    print(f"{n[0]:<6} {n[1]:<30} {desc_corta:<40} {fecha_formateada:<12}")
                print(f"\n\tTotal de notas: {len(notas)}")
            else:
                print("\t📭 No hay notas para mostrar.")
            funciones.esperarTecla()
            
        elif opcion == '3' or opcion == "CAMBIAR":
            funciones.borrarPantalla()
            print(f"\n \t .:: Modificar Nota ::. ")
            print(f"\tUsuario: {nombre} {apellidos}\n")
            
            notas = nota.mostrar(usuario_id)
            if notas:
                print(f"{'🔢 ID':<6} {'📌 TÍTULO':<30} {'📝 DESCRIPCIÓN':<40} {'📅 FECHA':<12}")
                print("═" * 90)
                for n in notas:
                    desc_corta = (n[2][:37] + '...') if len(n[2]) > 40 else n[2]
                    fecha_formateada = n[3].strftime('%d/%m/%Y') if n[3] else 'N/A'
                    print(f"{n[0]:<6} {n[1]:<30} {desc_corta:<40} {fecha_formateada:<12}")
                
                print("\n")
                id_nota = input("\tIngresa el ID de la nota a modificar (0 para cancelar): ")
                
                if id_nota == '0':
                    continue
                    
                if id_nota.isdigit():
                    id_nota = int(id_nota)
                    # Verificamos que la nota pertenezca al usuario
                    cursor.execute("SELECT id FROM notas WHERE id=%s AND usuario_id=%s", (id_nota, usuario_id))
                    nota_existe = cursor.fetchone()
                    
                    if nota_existe:
                        funciones.borrarPantalla()
                        print("\n \t .:: Editar Nota ::. ")
                        
                        # Obtener los datos actuales de la nota
                        cursor.execute("SELECT titulo, descripcion FROM notas WHERE id=%s AND usuario_id=%s", (id_nota, usuario_id))
                        nota_actual = cursor.fetchone()
                        
                        print(f"\n\tNota ID: {id_nota}")
                        print(f"\tTítulo actual: {nota_actual[0]}")
                        print(f"\tDescripción actual: {nota_actual[1]}\n")
                        
                        titulo = input(f"\tNuevo título (Enter para mantener actual): ")
                        descripcion = input(f"\tNueva descripción (Enter para mantener actual): ")
                        
                        # Mantener valores actuales si no se ingresan nuevos
                        titulo = titulo if titulo else nota_actual[0]
                        descripcion = descripcion if descripcion else nota_actual[1]
                        
                        resultado = nota.actualizar(id_nota, usuario_id, titulo, descripcion)
                        if resultado:
                            print("\n\t✅ Nota actualizada correctamente")
                        else:
                            print("\n\t❌ No se pudo actualizar la nota")
                    else:
                        print("\n\t⚠️ No existe una nota con ese ID o no te pertenece")
                else:
                    print("\n\t⚠️ El ID debe ser un número")
            else:
                print("\t📭 No hay notas para modificar.")
                
            funciones.esperarTecla()      
            
        elif opcion == '4' or opcion == "ELIMINAR":
            funciones.borrarPantalla()
            print(f"\n \t .:: Eliminar Nota ::. ")
            print(f"\tUsuario: {nombre} {apellidos}\n")
            
            notas = nota.mostrar(usuario_id)
            if notas:
                print(f"{'🔢 ID':<6} {'📌 TÍTULO':<30} {'📝 DESCRIPCIÓN':<40} {'📅 FECHA':<12}")
                print("═" * 90)
                for n in notas:
                    desc_corta = (n[2][:37] + '...') if len(n[2]) > 40 else n[2]
                    fecha_formateada = n[3].strftime('%d/%m/%Y') if n[3] else 'N/A'
                    print(f"{n[0]:<6} {n[1]:<30} {desc_corta:<40} {fecha_formateada:<12}")
                

                op=input("desea eliminar una nota?s/n")
                if op=="s":
                    print("\n")
                id_nota = input("\tIngresa el ID de la nota a eliminar: ")
                
                if id_nota == '0':
                    continue
                    
                if id_nota.isdigit():
                    id_nota = int(id_nota)
                    # Verificamos que la nota pertenezca al usuario
                    cursor.execute("SELECT id, titulo FROM notas WHERE id=%s AND usuario_id=%s", (id_nota, usuario_id))
                    nota_existe = cursor.fetchone()
                    
                    if nota_existe:
                        # Mostramos la nota que se va a eliminar
                        print("\n\tNota seleccionada para eliminar:")
                        print(f"\tID: {nota_existe[0]}")
                        print(f"\tTítulo: {nota_existe[1]}")
                        
                        # Preguntamos confirmación
                        confirmacion = input("\n\t¿Estás SEGURO que deseas ELIMINAR esta nota? (S/N): ").upper()
                        if confirmacion == "S":
                            resultado = nota.eliminar(id_nota, usuario_id)
                            if resultado:
                                print("\n\t✅ Nota eliminada correctamente")
                            else:
                                print("\n\t❌ No se pudo eliminar la nota")
                        else:
                            print("\n\tOperación cancelada")
                    else:
                        print("\n\t⚠️ No existe una nota con ese ID o no te pertenece")
                else:
                    print("\n\t⚠️ El ID debe ser un número")
            else:
                print("\t📭 No hay notas para eliminar.")
                
            funciones.esperarTecla()
            
        elif opcion == '5' or opcion == "SALIR":
            print("\n\tSesión terminada. ¡Hasta pronto!")
            break
        else:
            print("\n \t \t ⚠️ Opción no válida. Intenta de nuevo.")
            funciones.esperarTecla()
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\nOcurrió un error: {e}")
    finally:
        # Asegurarnos de cerrar la conexión al final
        if 'conexion' in globals() and conexion.is_connected():
            cursor.close()
            conexion.close()
            print("\nConexión a la base de datos cerrada.")
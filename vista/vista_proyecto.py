from modelo.Proyecto import Proyecto

from controlador.Controlador_proyecto import agregar_proyecto, eliminar_proyecto, buscar_proyecto,editar_proyecto,asignar_proyecto,desvincular_proyecto,registrar_tiempo
def menu_proyecto():
    print("____Menu Proyecto____")
    print("1. Crear Proyecto")
    print("2. Editar Proyecto")
    print("3. Buscar Proyecto")
    print("4. Eliminar Proyecto")
    print("5. Asignar Empleado a Proyecto ")
    print("6. Desvincular Empleado de Proyecto")
    print("7. Registrar Tiempo")
    print("0. Salir")
    opcion = int(input("Ingrese una opción: "))
    return opcion

# Aquí iría la función para agregar un proyecto
def add_proyecto():
    nombre_proyecto= input("Ingrese el nombre del proyecto: ")
    descripcion_proyecto = input("Ingrese la descripción del proyecto: ")
    fecha_inicio_proyecto = input("Ingrese la fecha de inicio del proyecto: ")
    proyecto =Proyecto(nombre_proyecto, descripcion_proyecto, fecha_inicio_proyecto)
    agregar_proyecto(proyecto)


# Aquí iría la función para editar un proyecto
def edit_proyecto():  # Aquí iría la función para editar un proyecto
    nombre_proyecto=input("Ingrese nombre del proyecto a editar: ")
    proyecto=buscar_proyecto(nombre_proyecto)
    if proyecto is not None:
        print("Menu de editar")
        print("1.-Nombre")
        print("2.-Descripción")
        print("3.-Fecha de inicio")
        print("0.-Salir")
        op=int(input("Seleccione una opcion: "))
        if op==1:
            print(f"El nombre actual es: {proyecto.get_nombre()}")
            nombre=input("Ingrese el nuevo nombre: ")
            proyecto.set_nombre(nombre)
        elif op==2:
            print(f"Su descripcion actual es: {proyecto.get_descripcion()}")
            descripcion=input("Ingrese la nueva descripcion: ")
            proyecto.set_descripcion(descripcion)
        elif op==3:
            print(f"Su fecha de inicio actual es: {proyecto.get_fecha_inicio()}")
            fecha_inicio=input("Ingrese la nueva fecha de inicio: ")
            proyecto.set_fecha_inicio(fecha_inicio)
        else:
            print("No se realizaron cambios")
        editar_proyecto(proyecto)
    else:
        print("No se encontró el proyecto")

# Aquí iría la función para buscar un proyecto
def search_proyecto():
    nombre = input("Ingrese nombre del Proyecto: ")
    proyecto = buscar_proyecto(nombre)
    if proyecto:
        print("===Proyecto encontrado===")
        print(proyecto)
    else:
        print("No se encontró el proyecto")
    return proyecto

# Aquí iría la función para eliminar un proyecto
def delete_proyecto():
    print("===Eliminar Proyecto===")
    try:
        nombre_proyecto = input("Ingrese nombre del proyecto a eliminar: ")
        proyecto = buscar_proyecto(nombre_proyecto)
        if proyecto  is not None:
            print(f"Eliminará la proyecto: {proyecto.get_nombre()}")
            print("¿Está seguro?")
            print("Si")
            print("No")
            resp=input("Seleccione una opción: ").strip()
            if resp.lower()=="si":
                eliminar_proyecto(proyecto)
            elif resp.lower() == "no":
                print("No se eliminó el proyecto")
            else:
                print("Opcion invalida. Operacion cancelada")
        else:
            print("Proyecto no encontrado")
    except Exception as e:
        print("Error al eliminar el proyecto: ", e)



def assign_proyecto(): # Aquí iría la función para asignar un proyecto a un empleado
    try:
        print("=== Asignar Proyecto ===")
        empleado_id = int(input("Ingrese el ID del empleado: "))
        proyecto_id = int(input("Ingrese el ID del proyecto: "))
        
        # Llama al controlador para realizar la asignación
        asignar_proyecto(empleado_id, proyecto_id)
        
    except ValueError:
        print("Error: Por favor, ingrese valores numéricos válidos para los IDs.")
    except Exception as e:
        print(f"Se produjo un error al asignar el proyecto: {e}")



def unassign_proyecto(): # Aquí iría la función para desvincular un proyecto de un empleado
    try:
        print("=== Desvincular Proyecto ===")
        empleado_id = int(input("Ingrese el ID del empleado: "))
        proyecto_id = int(input("Ingrese el ID del proyecto: "))

        desvincular_proyecto(empleado_id,proyecto_id)
    except ValueError:
        print("Error: Por favor, ingrese valores numéricos válidos para los IDs.")
    except Exception as e:
        print(f"Se produjo un error al desvincular el proyecto: {e}")

def record_time():
    try:
        print("=== Registrar Tiempo de Trabajo ===")
        id_empleado = int(input("Ingrese el ID del empleado: "))
        id_proyecto = int(input("Ingrese el ID del proyecto: "))
        fecha = input("Ingrese la fecha: ")
        horas_trabajadas = int(input("Ingrese la cantidad de horas trabajadas: "))
        descripcion_tarea = input("Ingrese una breve descripción de las tareas realizadas: ")

        # Llama al controlador para registrar el tiempo
        registrar_tiempo(id_empleado, id_proyecto, fecha, horas_trabajadas, descripcion_tarea)
        print("El tiempo trabajado ha sido registrado exitosamente.")
    except ValueError:
        print("Error: Por favor, ingrese datos válidos. Asegúrese de usar números para IDs y horas.")
    except Exception as e:
        print(f"Se produjo un error al registrar el tiempo: {e}")


def main_proyecto():
    opcion = -1
    while opcion != 0:
        opcion = menu_proyecto()
        if opcion == 1:
            add_proyecto()
        elif opcion == 2:
            edit_proyecto()
        elif opcion == 3:
            search_proyecto()
        elif opcion == 4:
            delete_proyecto()
        elif opcion == 5:
            assign_proyecto()
        elif opcion == 6:
            unassign_proyecto()
        elif opcion == 7:
            record_time()
        else:
            print("Opción no válida. Por favor, vuelva a intentarlo.")

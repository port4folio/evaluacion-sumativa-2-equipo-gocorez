from modelo.Proyecto import Proyecto
from controlador.Controlador_proyecto import agregar_proyecto, eliminar_proyecto, buscar_proyecto,editar_proyecto
def menu_proyecto():
    print("____Menu Proyecto____")
    print("1. Crear Proyecto")
    print("2. Editar Proyecto")
    print("3. Buscar Proyecto")
    print("4. Eliminar Proyecto")
    print("5. Asignar Proyecto")
    print("6. Desvincular Proyecto")
    opcion = int(input("Ingrese una opción: "))
    return opcion

# Aquí iría la función para agregar un proyecto
def add_proyecto():
    nombre_proyecto= input(print("Ingrese el nombre del proyecto: "))
    descripcion_proyecto = input(print("Ingrese la descripción del proyecto: "))
    fecha_inicio_proyecto = input(print("Ingrese la fecha de inicio del proyecto: "))
    proyecto =Proyecto(nombre_proyecto, descripcion_proyecto, fecha_inicio_proyecto)
    agregar_proyecto(proyecto)


# Aquí iría la función para editar un proyecto
def edit_proyecto():  # Aquí iría la función para editar un proyecto
    proyecto=buscar_proyecto()
    if proyecto is not None:
        print("Menu de editar")
        print("1.-Nombre")
        print("2.-Descripción")
        print("3.-Fecha de inicio")
        print("0.-Salir")
        op=int(input("Seleccione una opcion: "))
        if op==1:
            print(f"El nombre actual es: {proyecto.nombre()}")
            nombre=input("Ingrese el nuevo nombre: ")
            proyecto.set_nombre(nombre)
        elif op==2:
            print(f"Su descripcion actual es: {proyecto.descripcion()}")
            descripcion=input("Ingrese la nueva descripcion: ")
            proyecto.set_descripcion(descripcion)
        elif op==3:
            print(f"Su fecha de inicio actual es: {proyecto.fecha_inicio()}")
            fecha_inicio=input("Ingrese la nueva fecha de inicio: ")
            proyecto.set_fecha_inicio(fecha_inicio)
        else:
            print("No se realizaron cambios")
        editar_proyecto(proyecto)
    else:
        print("No se encontró el proyecto")

# Aquí iría la función para buscar un proyecto
def search_proyecto():
    nombre = input(print("Ingrese nombre del Proyecto: "))
    proyecto = Proyecto(nombre)
    return proyecto

# Aquí iría la función para eliminar un proyecto
def delete_proyecto():
    proyecto = buscar_proyecto()
    if proyecto  is not None:
        print(f"Eliminará la proyecto  {proyecto .get_nombre()}")
        print("¿Está seguro?")
        print("1.- Si")
        print("2.- No")
        print("3.- Salir")
        resp=int(input("Seleccione una opción: "))
        if resp==1:
            eliminar_proyecto(proyecto )
        else:
            print("Proyecto no eliminado")
    else:
        print("Proyecto no encontrado")


def asignar_proyecto():
    pass
# Aquí iría la función para asignar un proyecto a un empleado


def desvincular_proyecto():
    pass
# Aquí iría la función para desvincular un proyecto de un empleado


def main_proyecto():
    opcion = -1
    while opcion != 0:
        opcion = menu_proyecto()
        if opcion == 1:
            add_proyecto()
        elif opcion == 2:
            edit_proyecto()
        elif opcion == 3:
            buscar_proyecto()
        elif opcion == 4:
            delete_proyecto()
        elif opcion == 5:
            asignar_proyecto()
        elif opcion == 6:
            desvincular_proyecto()
        else:
            print("Opción no válida. Por favor, vuelva a intentarlo.")

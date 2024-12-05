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


def add_proyecto():
    pass
# Aquí iría la función para agregar un proyecto


def edit_proyecto():
    pass
# Aquí iría la función para editar un proyecto


def buscar_proyecto():
    pass
# Aquí iría la función para buscar un proyecto


def delete_proyecto():
    pass
# Aquí iría la función para eliminar un proyecto


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

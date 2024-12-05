

def menu_departamento():
    print("____Menu Departamento____")
    print("1. Ingresar Departamento")
    print("2. Editar Departamento")
    print("3. Buscar Departamento")
    print("4. Eliminar Departamento")
    print("5. Asignar Departamento")
    opcion = int(input("Ingrese una opción: "))
    return opcion


def add_departamento():
    pass
# Aquí iría la función para agregar un departamento

def edit_departamento():
    pass
# Aquí iría la función para editar un departamento

def buscar_departamento():
    pass
# Aquí iría la función para buscar un departamento

def delete_departamento():
    pass
# Aquí iría la función para eliminar un departamento

def asignar_departamento():
    pass
# Aquí iría la función para asignar un departamento a un empleado

def main_departamento():
    opcion = -1
    while opcion != 0:
        opcion = menu_departamento()
        if opcion == 1:
            add_departamento()
        elif opcion == 2:
            edit_departamento()
        elif opcion == 3:
            buscar_departamento()
        elif opcion == 4:
            delete_departamento()
        elif opcion == 5:
            asignar_departamento()
        else:
            print("Opción no válida. Por favor, vuelva a intentarlo.")




    
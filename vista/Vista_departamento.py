from modelo.Departamento import Departamento
from controlador.Controlador_departamento import agregar_departamento,editar_departamento,buscar_departamento,eliminar_departamento
def menu_departamento():
    print("____Menu Departamento____")
    print("1. Ingresar Departamento")
    print("2. Editar Departamento")
    print("3. Buscar Departamento")
    print("4. Eliminar Departamento")
    print("5. Asignar Departamento")
    print("0. Salir")
    opcion = int(input("Ingrese una opción: "))
    return opcion


def add_departamento():
    nombre = input("Ingrese el nombre del departamento: ")
    gerente=input("Ingrese gerente:")
    departamento=Departamento(nombre,gerente)
    agregar_departamento(departamento)

def edit_departamento(): # Aquí iría la función para editar un departamento
    departamento=buscar_departamento()
    if departamento is not None:
        print("Menu de edición")
        print("1. Editar nombre")
        print("2. Editar gerente")
        print("0. Salir")
        op=int(input("Seleccione una opción:"))
        if op==1:
            print(f"El nombre actual es: {departamento.get_nombre()}")
            nombre=input("Ingrese nuevo nombre: ")
            departamento.set_nombre(nombre)
        elif op==2:
            print(f"El gerente actual es: {departamento.get_gerente()}")
            gerente=input("Ingrese nuevo gerente: ")
            departamento.set_gerente(gerente)
        else:
            print("No se realizaron cambios")
        editar_departamento(departamento)
    else:
        print("departamento no encontrado")

def search_departamento():# Aquí iría la función para buscar un departamento
    nombre=input("Ingrese el nombre del departamento a buscar: ")
    departamento=buscar_departamento(nombre)
    return(departamento)

def delete_departamento(): # Aquí iría la función para eliminar un departamento
    departamento=search_departamento()
    if departamento is not None:
        print(f"Eliminar departamento {departamento.get_nombre()}")
        print("¿Esta Seguro?")
        print("1.-Si")
        print("2.-No")
        print("3.-Salir")
        resp=int(input("Seleccione una opción: "))
        if resp==1:
            eliminar_departamento(departamento)
        else:
            print("Departamento no eliminado")
    else:
        print("Departamento no encontrado")

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




    
from controlador.Controlador_empleado import agregar_empleado, linea_divisora_menu
from modelo.Empleado import Empleado


def menu():
    linea_divisora_menu()
    print("Menu Empleado")
    linea_divisora_menu()
    print("1. Registrar Empleado")
    print("2. Editar Empleado")
    print("3. Eliminar Empleado")
    print("0. Salir")
    op = int(input("Ingrese una opción: "))
    return op 

def add_empleado():
    nombre = input("Ingrese el nombre del empleado: ")
    apellido = input("Ingrese el apellido del empleado: ")
    direccion = input("Ingrese la dirección del empleado: ")
    telefono = input("Ingrese el teléfono del empleado: ")
    fecha_inicio_contrato = input("Ingrese la fecha de inicio del contrato: ")
    salario = input("Ingrese el salario del empleado: ")
    empleado = Empleado(nombre, apellido, direccion, telefono, None, fecha_inicio_contrato, salario )
    agregar_empleado(empleado)
   
    
def edit_empleado():
    pass

def delete_empleado():
    pass

def main_empleado():
    op = -1
    while op != 0:
        op = menu()
        if op == 1:
            add_empleado()
        elif op == 2:
            edit_empleado()
        elif op == 3:
            delete_empleado()
from controlador.Controlador_empleado import agregar_empleado
from modelo.Empleado import Empleado

def menu():
    print("Menu Empleado")
    print("1. Registrar Empleado")
    print("2. Editar Empleado")
    print("3. Eliminar Empleado")
    print("0. Salir")
    op = int(input("Ingrese una opción: "))
    return op 

def add_empleado():
    nombre = input("Ingrese el nombre del empleado: ")
    direccion = input("Ingrese la dirección del empleado: ")
    telefono = input("Ingrese el teléfono del empleado: ")
    email = input("Ingrese el correo del empleado: ")
    fecha_inicio_contrato = input("Ingrese la fecha de inicio del contrato: ")
    salario = input("Ingrese el salario del empleado: ")
    empleado = Empleado(nombre, direccion, telefono, email, fecha_inicio_contrato, salario )
    agregar_empleado(empleado)
   
    


def main_empleado():
    op = -1
    while op != 0:
        op = menu()
        if op == 1:
            add_empleado()
      
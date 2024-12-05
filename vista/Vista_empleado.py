from controlador.Controlador_empleado import agregar_empleado 
from modelo.Empleado import Empleado

def menu_empleado():
    print("____Menu Empleado____")
    print("1. Registrar Empleado")
    print("2. Editar Empleado")
    print("3. Eliminar Empleado")
    print("4. Registrar horas trabajadas")
    print("5. Asignar Proyecto")
    print("6. Reasignar Proyecto")
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

def registrar_tiempo():
    pass

def asignar_proyecto():
    pass

def reasignar_proyecto():
    pass

def main_empleado():
    op = -1
    while op != 0:
        op = menu_empleado()
        if op == 1:
            add_empleado()
        elif op == 2:
            edit_empleado()
        elif op == 3:
            delete_empleado()
        elif op == 4:
            registrar_tiempo()
        elif op == 5:
            asignar_proyecto()
        elif op == 6:
            reasignar_proyecto()
        else:
            print("Opción no válida")
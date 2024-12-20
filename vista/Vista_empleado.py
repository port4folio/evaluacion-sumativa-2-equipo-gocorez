from controlador.Controlador_empleado import agregar_empleado,eliminar_empleado, buscar_empleado,actualizar_empleado,generar_email_unico
from modelo.Empleado import Empleado

def menu_empleado():
    print("===== Menu Empleado =====")
    print("1. Registrar Empleado")
    print("2. Editar Empleado")
    print("3. Eliminar Empleado")
    print("0. Salir")
    print("=========================")
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
    print("=== Editar Empleado ===")
    try:
        # Solicitar el nombre del empleado a editar
        nombre_empleado = input("Ingrese el nombre del empleado a editar: ")

        # Llamar al controlador para buscar el empleado
        empleado = buscar_empleado(nombre_empleado)
        if not empleado:
            print("No se encontró un empleado con ese nombre.")
            return

        # Mostrar los datos actuales del empleado (sin el email, ya que es automático)
        print(f"Empleado encontrado: ID: {empleado.get_id()}, Nombre: {empleado.get_nombre()}, Apellido: {empleado.get_apellido()}, "
              f"Dirección: {empleado.get_direccion()}, Teléfono: {empleado.get_telefono()}, Email: {empleado.get_email()}, "
              f"Fecha de inicio: {empleado.get_fecha_inicio_contrato()}, Salario: {empleado.get_salario()}")
        # Solicitar los nuevos datos del empleado
        nuevo_nombre = input("Ingrese el nuevo nombre del empleado (presione Enter para mantener el actual): ")
        nuevo_apellido = input("Ingrese el nuevo apellido del empleado (presione Enter para mantener el actual): ")
        nueva_direccion = input("Ingrese la nueva dirección del empleado (presione Enter para mantener la actual): ")
        nuevo_telefono = input("Ingrese el nuevo teléfono del empleado (presione Enter para mantener el actual): ") 
        nueva_fecha_inicio = input("Ingrese la nueva fecha de inicio de contrato del empleado (YYYY/MM/DD), presione Enter para mantener la actual): ")
        nuevo_salario = input("Ingrese el nuevo salario del empleado (presione Enter para mantener el actual): ")
        # Actualizar los datos del empleado
        if nuevo_nombre:
            empleado.set_nombre(nuevo_nombre)
        if nuevo_apellido:
            empleado.set_apellido(nuevo_apellido)
        if nueva_direccion:
            empleado.set_direccion(nueva_direccion)
        if nuevo_telefono:
            empleado.set_telefono(nuevo_telefono)
        if nueva_fecha_inicio:
            empleado.set_fecha_inicio_contrato(nueva_fecha_inicio)
        if nuevo_salario:
            empleado.set_salario(nuevo_salario)

        nuevo_email = generar_email_unico(nuevo_nombre,nuevo_apellido) 
        empleado.set_email(nuevo_email)
        # Llamar al controlador para actualizar el empleado
        actualizar_empleado(empleado)
    except ValueError:
        print("Error: Por favor ingrese valores válidos.")
    except Exception as e:
        print(f"Error al editar empleado: {e}")



def delete_empleado():
    print("____Eliminar Empleado____")
    nombre = input("Ingrese el nombre del empleado: ")
    empleado = buscar_empleado(nombre)  # Método en controlador_empleado
    if empleado is not None:
        print("Empleado encontrado:")
        print(f"Nombre: {empleado.get_nombre()}")
        print(f"Apellido: {empleado.get_apellido()}")
        print(f"Dirección: {empleado.get_direccion()}")
        print(f"Teléfono: {empleado.get_telefono()}")
        print(f"Email: {empleado.get_email()}")
        print(f"Fecha de inicio de contrato: {empleado.get_fecha_inicio_contrato()}")
        print(f"Salario: {empleado.get_salario()}")
        
        confirmacion = input("¿Está seguro de que desea eliminar este empleado? (s/n): ")
        if confirmacion.lower() == 's':
            eliminar_empleado(empleado)  # Método en controlador_empleado para eliminar
        else:
            print("Eliminación cancelada")
    else:
        print("Empleado no encontrado")


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
        else:
            print("Opción no válida")
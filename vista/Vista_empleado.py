from controlador.Controlador_empleado import agregar_empleado,eliminar_empleado, buscar_empleado_email, buscar_empleado_id, buscar_empleado_nombre, actualizar_empleado,registrar_tiempo 
from modelo.Empleado import Empleado

def menu_empleado():
    print("____Menu Empleado____")
    print("1. Registrar Empleado")
    print("2. Editar Empleado")
    print("3. Eliminar Empleado")
    print("4. Registrar horas trabajadas")
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
    print("____Editar Empleado____")
    print("Seleccione una opción de búsqueda:")
    print("1. Buscar por Nombre")
    print("2. Buscar por Email")
    print("3. Buscar por ID")
    opción = int(input("Ingrese una opción: "))
    empleado = None
    if opción == 1:
        nombre = input("Ingrese el nombre del empleado: ")
        empleado = buscar_empleado_nombre(nombre)  # Método en controlador_empleado
    elif opción == 2:
        email = input("Ingrese el email del empleado: ")
        empleado = buscar_empleado_email(email)  # Método en controlador_empleado
    elif opción == 3:
        id_empleado = input("Ingrese el ID del empleado: ")
        empleado = buscar_empleado_id(id_empleado)  # Método en controlador_empleado
    else:
        print("Opción no válida")
        return
    if empleado is not None:
        print("Empleado encontrado:")
        print(f"Nombre: {empleado.get_nombre()}")
        print(f"Apellido: {empleado.get_apellido()}")
        print(f"Dirección: {empleado.get_direccion()}")
        print(f"Teléfono: {empleado.get_telefono()}")
        print(f"Email: {empleado.get_email()}")
        print(f"Fecha de inicio de contrato: {empleado.get_fecha_inicio_contrato()}")
        print(f"Salario: {empleado.get_salario()}")
        
        # Permitir al usuario modificar los campos
        nuevo_nombre = input("Ingrese el nuevo nombre (dejar en blanco para no cambiar): ")
        nuevo_apellido = input("Ingrese el nuevo apellido (dejar en blanco para no cambiar): ")
        nuevo_direccion = input("Ingrese la nueva dirección (dejar en blanco para no cambiar): ")
        nuevo_telefono = input("Ingrese el nuevo teléfono (dejar en blanco para no cambiar): ")
        nuevo_email = input("Ingrese el nuevo email (dejar en blanco para no cambiar): ")
        nuevo_fecha_inicio_contrato = input("Ingrese la nueva fecha de inicio de contrato (dejar en blanco para no cambiar): ")
        nuevo_salario = input("Ingrese el nuevo salario (dejar en blanco para no cambiar): ")
        
        # Actualizar solo los campos que no están en blanco
        if nuevo_nombre:
            empleado.set_nombre(nuevo_nombre)
        if nuevo_apellido:
            empleado.set_apellido(nuevo_apellido)
        if nuevo_direccion:
            empleado.set_direccion(nuevo_direccion)
        if nuevo_telefono:
            empleado.set_telefono(nuevo_telefono)
        if nuevo_email:
            empleado.set_email(nuevo_email)
        if nuevo_fecha_inicio_contrato:
            empleado.set_fecha_inicio_contrato(nuevo_fecha_inicio_contrato)
        if nuevo_salario:
            empleado.set_salario(nuevo_salario)
        
        # Llamar al método para actualizar el empleado
        actualizar_empleado(empleado)  # Método en controlador_empleado
    else:
        print("Empleado no encontrado")

def delete_empleado():
    print("____Eliminar Empleado____")
    print("Seleccione una opción de búsqueda:")
    print("1. Buscar por Nombre")
    print("2. Buscar por Email")
    print("3. Buscar por ID")
    opción = int(input("Ingrese una opción: "))
    empleado = None
    if opción == 1:
        nombre = input("Ingrese el nombre del empleado: ")
        empleado = buscar_empleado_nombre(nombre)  # Método en controlador_empleado
    elif opción == 2:
        email = input("Ingrese el email del empleado: ")
        empleado = buscar_empleado_email(email)  # Método en controlador_empleado
    elif opción == 3:
        id_empleado = input("Ingrese el ID del empleado: ")
        empleado = buscar_empleado_id(id_empleado)  # Método en controlador_empleado
    else:
        print("Opción no válida")
        return
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
            eliminar_empleado(empleado.get_id())  # Método en controlador_empleado para eliminar
            print("Empleado eliminado")
        else:
            print("Eliminación cancelada")
    else:
        print("Empleado no encontrado")

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
            record_time()
        else:
            print("Opción no válida")
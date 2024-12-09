from modelo.Departamento import Departamento
from controlador.Controlador_departamento import agregar_departamento,editar_departamento,buscar_departamento,eliminar_departamento,asignar_empleado_a_departamento,reasignar_empleado_a_departamento,obtener_empleados_por_departamento,actualizar_departamento
def menu_departamento():
    print("____Menu Departamento____")
    print("1. Ingresar Departamento")
    print("2. Editar Departamento")
    print("3. Buscar Departamento")
    print("4. Eliminar Departamento")
    print("5. Asignar Departamento")
    print("6. Reasignar Departamento")
    print("0. Salir")
    opcion = int(input("Ingrese una opción: "))
    return opcion


def add_departamento():
    nombre = input("Ingrese el nombre del departamento: ")
    gerente=input("Ingrese gerente:")
    departamento=Departamento(nombre,gerente)
    agregar_departamento(departamento)

def edit_departamento(): # Aquí iría la función para editar un departamento
    try:
        nombre_departamento=input("Ingrese el nombre del departamento que desea editar:")
        departamento=buscar_departamento(nombre_departamento)
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
            actualizar_departamento(departamento)
        else:
            print("departamento no encontrado")
    except ValueError:
        print("Error: Por favor ingrese valores válidos.")
    except Exception as e:
        print(f"Error al editar departamento: {e}")

def search_departamento():
    nombre = input("Ingrese el nombre del departamento a buscar: ")
    departamento = buscar_departamento(nombre)
    if departamento:
        print("=== Departamento Encontrado ===")
        print(departamento)  # Llama al método __str__ del modelo Departamento
    else:
        print("No se encontró un departamento con ese nombre.")
    return departamento

def delete_departamento(): # Aquí iría la función para eliminar un departamento
    nombre=input("Ingrese nombre del departamento a eliminar:")
    departamento=buscar_departamento(nombre)
    if departamento is not None:
        print(f"Eliminar departamento {departamento.get_nombre()}")
        print("¿Esta Seguro?")
        print("1.-Si")
        print("2.-No")
        print("3.-Salir")
        resp=int(input("Seleccione una opción: "))
        if resp == 1:
            eliminar_departamento(departamento)

def delete_departamento():
    print("=== Eliminar Departamento ===")
    try:
        # Solicitar el nombre del departamento a eliminar
        nombre = input("Ingrese el nombre del departamento a eliminar: ")
        
        # Buscar el departamento
        departamento = buscar_departamento(nombre)
        
        if departamento is not None:
            print(f"Departamento encontrado: {departamento.get_nombre()}")
            print("¿Está seguro que desea eliminarlo?")
            print("Si")
            print("No")
            
            # Solicitar confirmación
            resp = input("Seleccione una opción: ").strip()
            if resp.lower() == "si":
                # Llamar al método para eliminar el departamento
                eliminar_departamento(departamento)
            elif resp.lower() == "no":
                print("Operación cancelada.")
            else:
                print("Opción inválida. Operación cancelada.")

        else:
            print("Departamento no encontrado.")
    except Exception as e:
        print(f"Error al eliminar el departamento: {e}")


def vista_asignar_empleado_departamento(): # Aquí iría la función para asignar un departamento a un empleado
    print("=== Asignar Empleado a un Departamento ===")
    try:
        # Solicitar datos al usuario
        id_empleado = int(input("Ingrese el ID del empleado: "))
        id_departamento = int(input("Ingrese el ID del departamento: "))
        # Llamar al controlador para asignar el empleado
        asignar_empleado_a_departamento(id_empleado, id_departamento)
        print("Empleado asignado al departamento exitosamente.")
    except ValueError:
        print("Error: Por favor ingrese valores numéricos válidos.")
    except Exception as e:
        print(f"Error al asignar empleado al departamento: {e}")


def vista_reasignar_empleado_departamento():# Aquí iría la función para reasignar un departamento a un empleado
    print("=== Reasignar Empleado a otro Departamento ===")
    try:
        # Solicitar datos al usuario
        id_empleado = int(input("Ingrese el ID del empleado: "))
        id_departamento = int(input("Ingrese el nuevo ID del departamento: "))
        # Llamar al controlador para reasignar el empleado
        reasignar_empleado_a_departamento(id_empleado, id_departamento)
        print("Empleado reasignado exitosamente.")
    except ValueError:
        print("Error: Por favor ingrese valores numéricos válidos.")
    except Exception as e:
        print(f"Error al reasignar empleado al departamento: {e}")

def vista_mostrar_empleados_por_departamento():
    print("=== Mostrar Empleados por Departamento ===")
    try:
        # Solicitar el ID del departamento
        id_departamento = int(input("Ingrese el ID del departamento: "))

        # Llamar al controlador para obtener los empleados
        empleados = obtener_empleados_por_departamento(id_departamento)

        # Mostrar los resultados
        if empleados:
            print(f"Empleados en el Departamento {id_departamento}:")
            for empleado in empleados:
                print(f"- ID: {empleado[0]}, Nombre: {empleado[1]}")
        else:
            print("No hay empleados asignados a este departamento.")
    except ValueError:
        print("Error: Por favor ingrese un valor numérico válido.")
    except Exception as e:
        print(f"Error al mostrar empleados por departamento: {e}")


def main_departamento():
    opcion = -1
    while opcion != 0:
        opcion = menu_departamento()
        if opcion == 1:
            add_departamento()
        elif opcion == 2:
            edit_departamento()
        elif opcion == 3:
            search_departamento()
        elif opcion == 4:
            delete_departamento()
        elif opcion == 5:
            vista_asignar_empleado_departamento()
        elif opcion == 6:
            vista_reasignar_empleado_departamento()
        elif opcion == 7:
            vista_mostrar_empleados_por_departamento()
        else:
            print("Opción no válida. Por favor, vuelva a intentarlo.")




    
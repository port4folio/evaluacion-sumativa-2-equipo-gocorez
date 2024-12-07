def menu_informes():
    print("__Menu Informe__")
    print("1. Mostrar empleados")
    print("2. Mostrar Proyectos")
    print("3. Mostrar Departamentos")
    print("4. Mostrar Registro Tiempo")
    opcion = int(input("Ingrese una opción: "))
    return opcion

def mostrar_empleados():
    print("##### Mostrando informe de empleados: #####")## pendiente llamar al metodo empleado. 


def mostrar_proyectos():# proyecto
    print("###### Mostrando informe de proyectos: ######")

def mostrar_departamentos():# Departamento 
    print("###### Mostrando informe de departamentos: ######")

def mostrar_registro_tiempo():#3 empleado 
    print("###### Mostrando informe de registro de tiempo ######")


def main_informes():
    op=-1
    while op!=0:
        op=menu_informes()
        if op==1:
            mostrar_empleados()
        elif op==2:
            mostrar_proyectos()
        elif op==3:
            mostrar_departamentos()
        elif op==4:
            mostrar_registro_tiempo()
            
from modelo.Empleado import Empleado
from controlador.Controlador_empleado import mostrar_empleados
from controlador.Controlador_proyecto import mostrar_proyectos,mostrar_registro_tiempo 
from controlador.Controlador_departamento import mostrar_departamentos

def menu_informes():
    print("__Menu Informe__")
    print("1. Mostrar empleados")
    print("2. Mostrar Proyectos")
    print("3. Mostrar Departamentos")
    print("4. Mostrar Registro Tiempo")
    print("0. Salir")
    opcion = int(input("Ingrese una opción: "))
    return opcion

def view_empleados():
    empleados=mostrar_empleados()
    if len(empleados)>0:
        for empleado in empleados:
            print(empleado)
    else:
        print("No hay empleados registrados")
 
def view_proyectos():# proyecto
    proyectos=mostrar_proyectos()
    if len(proyectos)>0:
        for proyecto in proyectos:
            print(proyecto)
    else:
        print("No hay proyectos registrados")

def view_departamentos():# Departamento 
    departamentos=mostrar_departamentos()
    if len(departamentos)>0:
        for departamento in departamentos:
            print(departamento)
    else:
        print("No hay departamentos registrados")

def view_registro_tiempo():#3 empleado 
    registro_tiempo=mostrar_registro_tiempo()
    if len(registro_tiempo)>0:
        for registro in registro_tiempo:
            print(registro) 
    else:
        print("No hay registros de tiempo")

def main_informes():
    op=-1
    while op!=0:
        op=menu_informes()
        if op==1:
            view_empleados()
        elif op==2:
            view_proyectos()
        elif op==3:
            view_departamentos()
        elif op==4:
            view_registro_tiempo()
            
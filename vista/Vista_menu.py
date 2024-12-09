from vista.Vista_empleado import main_empleado
from vista.Vista_departamento import main_departamento
from vista.vista_proyecto import main_proyecto
from vista.Vista_informes import main_informes
import os

def limpiar_consola():
        os.system('cls')   

def menu_principal():
    limpiar_consola()
    print("##### Menu Principal ##### ")
    print("____Elija una opción____")
    print("1.- Menu Empleados")
    print("2.- Menu Departamentos")
    print("3.- Menu Proyectos")
    print("4.- Informes")
    print("===========================")
    opcion = int(input("Ingrese una opcion: "))
    return opcion
    
while True:
   
    opcion = menu_principal()
    if opcion == 1:
        main_empleado()
    elif opcion == 2:
        main_departamento()
    elif opcion == 3:
        main_proyecto()
    elif opcion == 4:
        main_informes()
    break  
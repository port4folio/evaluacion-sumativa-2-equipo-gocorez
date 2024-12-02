from vista.Vista_empleado import main_empleado
from controlador.Controlador_empleado import linea_divisora_menu
import os

def limpiar_consola():
    os.system('cls')   

def menu():
    limpiar_consola()
    linea_divisora_menu()
    print("Menu Principal")
    linea_divisora_menu()
    print("____Elija una opción____")
    print("1.- Menu Empleados")
    opcion = int(input("Ingrese una opcion: "))
    return opcion
    
while True:
   
    opcion = menu()
    if opcion == 1:
        main_empleado()
    break  
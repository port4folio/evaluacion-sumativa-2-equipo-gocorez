from vista.Vista_empleado import main_empleado
import os

def limpiar_consola():
    os.system('cls')  

def menu():
    print("Menu Principal")
    print("1.- Empleados")
    op = int(input("Ingrese una opcion: "))
    return op
    
while True:
   
    op = menu()
    if op == 1:
        main_empleado()
    break  
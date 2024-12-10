#En esta clase lo necesario para poder hacer las consultas en en el controlador y poder registrar en él de ser necesario
import json
from controlador.Controlador_indicadores import traer_indicadores
def menu_indicadores():
    print("1.- Mostrar valor uf")
    print("2.- Mostrar valor ivp")
    print("3.- Mostrar valor ipc")
    print("4.- Mostrar valor utm")
    print("5.- Mostrar valor dolar")
    print("6.- Mostrar valor euro")
    print("0.- Salir")
    op=int(input("Ingrese una opción: "))
    return op

def mostrar_uf():
    indicadores=traer_indicadores()
    print(json.dumps(indicadores,indent=4))
    print(indicadores['uf']['valor'])

def mostrar_ivp():
    indicadores=traer_indicadores()
    print(json.dumps(indicadores,indent=4))
    print(indicadores['ivp']['valor'])

def mostrar_ipc():
    indicadores=traer_indicadores()
    print(json.dumps(indicadores,indent=4))
    print(indicadores['ipc']['valor'])

def mostrar_utm():
    indicadores=traer_indicadores()
    print(json.dumps(indicadores,indent=4))
    print(indicadores['utm']['valor'])

def mostrar_dolar():
    indicadores=traer_indicadores()
    print(json.dumps(indicadores,indent=4))
    print(indicadores['dolar']['valor'])

def mostrar_euro():
    indicadores=traer_indicadores()
    print(json.dumps(indicadores,indent=4))
    print(indicadores['euro']['valor'])

def main_indicadores():
    while True:
        op=menu_indicadores()
        if op==1:
            mostrar_uf()
        elif op==2:
            mostrar_ivp()
        elif op==3:
            mostrar_ipc()
        elif op==4:
            mostrar_utm()
        elif op==5:
            mostrar_dolar()
        elif op==6:
            mostrar_euro()
        elif op==0:
            print("Gracias por preferirnos")
            break

#En esta clase lo necesario para poder hacer las consultas en en el controlador y poder registrar en él de ser necesario
#import json
from controlador.Controlador_indicadores import traer_indicador_por_fecha
def mostrar_menu():
    print("Seleccione el indicador económico:")
    print("1. Unidad de Fomento (UF)")
    print("2. Índice de valor Promedio (IVP)")
    print("3. Índice de Precio al Consumidor (IPC)")
    print("4. Unidad Tributaria Mensual (UTM)")
    print("5. Dólar Observado")
    print("6. Euro")
    opcion = input("Ingrese el número de la opción: ")

    indicadores = {
        "1": "uf",
        "2": "ivp",
        "3": "ipc",
        "4": "utm",
        "5": "dolar",
        "6": "euro"
    }

    indicador = indicadores.get(opcion)
    if not indicador:
        print("Opción no válida")
        return

    fecha = input("Ingrese la fecha  : ")

    datos = traer_indicador_por_fecha(indicador, fecha )
    if datos:
        print("Datos obtenidos:", datos)



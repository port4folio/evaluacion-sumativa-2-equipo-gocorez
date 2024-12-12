#En esta clase lo necesario para poder hacer las consultas en en el controlador y poder registrar en él de ser necesario
#import json
from controlador.Controlador_indicadores import traer_indicador_por_fecha,agregar_consulta
from modelo.Indicadores import Indicadores ## Agregado Recien SF
from datetime import datetime ## Agregado recien SF
def mostrar_menu(usuario):
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

        indicador_obj = Indicadores(
            nombre_indicador=indicador,
            fecha_indicador=fecha,
            fecha_consulta=datetime.now().strftime('%Y-%m-%d'),  # Fecha actual de la consulta
            usuario_consulta=1,  # Asumimos que el usuario es 1, puedes ajustar según sea necesario
            sitio_consulta='mindicador.cl'
        )

        # Registrar la consulta en la base de datos
        agregar_consulta(indicador_obj,usuario)
    else:
        print("No se pudieron obtener los datos del indicador.")



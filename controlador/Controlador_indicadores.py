import requests
import json
from datetime import datetime
 
def traer_indicador_por_fecha(indicador, fecha):
    # Validar y formatear la fecha al formato dd-mm-yyyy
    try:
        fecha_formateada = datetime.strptime(fecha, '%Y-%m-%d').strftime('%d-%m-%Y')
    except ValueError:
        print("Error: El formato de 'fecha' debe ser YYYY-MM-DD.")
        return None
 
    # Construir el URL para la consulta
    url = f"https://mindicador.cl/api/{indicador}/{fecha_formateada}"
    # Realizar la solicitud
    response = requests.get(url)
    if response.status_code == 200:
        # Parsear la respuesta y devolver el resultado en formato JSON bonito
        datos = json.loads(response.text)
        pretty_json = json.dumps(datos, indent=4)
        return pretty_json
    else:
        print(f"Error al realizar la solicitud (código {response.status_code}): {response.text}")
        return None
 

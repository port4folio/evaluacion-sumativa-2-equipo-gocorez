import requests
import json
from datetime import datetime
from modelo.ConexionBD import conectar
from modelo.Indicadores import Indicadores ## ver esto
 
def agregar_consulta(indicadores):
    conn=conectar()
    try:
        if conn is not None:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO registro_indicadores ( nombre_indicador,fecha_indicador,fecha_consulta,usuario_consulta,sitio_consulta) VALUES (%s,%s,%s,%s,%s)",
                (indicadores.get_nombre_indicador(),indicadores.get_fecha_indicador(),indicadores.get_fecha_consulta(),indicadores.get_usuario_consulta(),indicadores.get_sitio_consulta())
            )
            conn.commit()
            print("Consulta ingresada exitosamente. ")
    except Exception as e:
        print(f"Error al ingresar la consulta: {e}")
    finally:
        cursor.close()
        conn.close()

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
 


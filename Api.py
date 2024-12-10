import json
import requests
 
class Mindicador:
 
    def __init__(self, indicador, year):
        self.indicador = indicador
        self.year = year
    
    def InfoApi(self):
        # En este caso hacemos la solicitud para el caso de consulta de un indicador en un año determinado
        url = f'https://mindicador.cl/api/{self.indicador}/{self.year}'
        response = requests.get(url)
        data = json.loads(response.text.encode("utf-8"))
        # Para que el json se vea ordenado, retornar pretty_json
        pretty_json = json.dumps(data, indent=2)
        return pretty_json
import requests
def traer_indicadores(indicador):
    url = "https://mindicador.cl/api/{indicador}"
    indicador=requests.get(url).json()
    return indicador
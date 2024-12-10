import requests
def traer_indicadores():
    indicadores=requests.get("https://mindicador.cl/api").json()
    return indicadores
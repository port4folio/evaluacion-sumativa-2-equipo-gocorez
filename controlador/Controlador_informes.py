from modelo.ConexionBD import conectar
from modelo.Informe import Informes
from Controlador_informes import mostrar_empleados

def mostrar_empleados(Informe):
    conn=conectar()
    

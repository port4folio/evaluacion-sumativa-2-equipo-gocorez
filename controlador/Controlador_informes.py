from modelo.ConexionBD import conectar
from modelo.Informe import Informes
from Controlador_informes import mostrar_empleados

def mostrar_empleados(Informe):
    conn=conectar()
    try:
        if conn is not None:
            cursor=conn.cursor()
            cursor.execute("SELECT id, nombre, apellido, direccion, telefono, email, fecha_inicio_contrato, salario FROM empleados")
            empleados_encontrados=cursor.fetchall()
            empleados=[]
            if len(empleados_encontrados)>0:
                for empleado in empleados_encontrados:
                    empleado_encontrado=Empleado()
                    
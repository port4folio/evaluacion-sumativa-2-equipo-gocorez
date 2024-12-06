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
                    empleado_encontrado=Empleado(empleado[1],empleado[2],empleado[3],empleado[4],empleado[5],empleado[6],empleado[7])
                    empleado_encontrado.set_id(empleado[0])
                    empleados.append(empleado_encontrado)
                return empleados
            else:
                return None
        else:
            return None
    except Exception as e:
        print(f"Error al conectar. {e}")
    finally:
        cursor.close()
        conn.close()
    
                


                    
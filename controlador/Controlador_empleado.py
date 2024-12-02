from modelo.ConexionBD import conectar
from modelo.Empleado import Empleado




def agregar_empleado(empleado):
    conn = conectar()
    try:
        if conn is not None:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO empleado (nombre, direccion, telefono, email, fecha_inicio_contrato, salario ) VALUES (%s, %s, %s, %s, %s, %s )",(empleado.get_nombre(), 
            empleado.get_direccion(),empleado.get_telefono(), empleado.get_email(), empleado.get_fecha_inicio_contrato(), empleado.get_salario()))
            conn.commit()
            print("Empleado ingresado con éxito")
    except Exception as e:
        print("Error al agregar empleado {e} ")
    finally:
        cursor.close()
        conn.close




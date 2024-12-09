from modelo.ConexionBD import conectar
from modelo.Empleado import Empleado

def generar_email_unico(nombre, apellido):
    base_email = f"{nombre.lower()}.{apellido.lower()}@ecotech.com"
    email = base_email
    contador = 1

    conn = conectar()
    try:
        cursor = conn.cursor()
        while email_existe(cursor, email):
            email = f"{base_email.split('@')[0]}{contador}@ecotech.com"
            contador += 1
    finally:
        cursor.close()
        conn.close()
    
    return email

def email_existe(cursor, email):
    cursor.execute("SELECT COUNT(*) FROM empleado WHERE email = %s", (email,))
    return cursor.fetchone()[0] > 0

def agregar_empleado(empleado):
    conn = conectar()
    try:
        if conn is not None:
            cursor = conn.cursor()
            # Generar el email único
            email = generar_email_unico(empleado.get_nombre(), empleado.get_apellido())
            # Actualizar el email en el objeto empleado
            empleado.set_email(email)

            cursor.execute("INSERT INTO empleado (nombre, apellido, direccion, telefono, email, fecha_inicio_contrato, salario) VALUES (%s, %s, %s, %s, %s, %s,%s)",
                           (empleado.get_nombre(), 
                            empleado.get_apellido(),
                            empleado.get_direccion(),
                            empleado.get_telefono(), 
                            empleado.get_email(), 
                            empleado.get_fecha_inicio_contrato(), 
                            empleado.get_salario()))
            conn.commit()
            print("Empleado ingresado con éxito")
    except Exception as e:
        print(f"Error al agregar empleado: {e}")
    finally:
        cursor.close()
        conn.close()

def actualizar_empleado(empleado):
    conn = conectar()
    try:
        if conn is not None:
            cursor = conn.cursor()
            cursor.execute("UPDATE empleado SET nombre=%s, apellido=%s, direccion=%s, telefono=%s, email=%s, fecha_inicio_contrato=%s, salario=%s WHERE id_empleado=%s",
                           (empleado.get_nombre(),
                            empleado.get_apellido(),
                            empleado.get_direccion(),
                            empleado.get_telefono(),
                            empleado.get_email(),
                            empleado.get_fecha_inicio_contrato(),
                            empleado.get_salario(),
                            empleado.get_id()))
            conn.commit()
            print("Empleado actualizado")
    except Exception as e:
        print(f"No se actualizaron registros: {e}")
    finally:
        cursor.close()
        conn.close()

def eliminar_empleado(empleado):
    conn=conectar()
    try:
        if conn is not None:
            cursor=conn.cursor()
            cursor.execute("DELETE FROM empleado WHERE id_empleado=%s",
                        (empleado.get_id(),))
            conn.commit()
            print("Empleado eliminado")
    except Exception as e:
        print(f"No se eliminaron registros {e}")
    finally:
        cursor.close()
        conn.close()

def buscar_empleado(nombre):
    conn=conectar()
    try:
        if conn is not None:
            cursor=conn.cursor()
            cursor.execute(
                "SELECT * FROM empleado WHERE nombre=%s",
                (nombre,))
            empleado = cursor.fetchone()
            if empleado  is not None:
                empleado_encontrado=Empleado(empleado [1],empleado [2],empleado [3],empleado [4],empleado [5],empleado[6],empleado[7])
                empleado_encontrado.set_id(empleado [0])
            else:
                empleado_encontrado=None
            return empleado_encontrado
        else:
            return None
    except Exception as e:
        print(f"Error al conectar. {e}")
    finally:
        cursor.close()
        conn.close()

def obtener_empleados():
    conn=conectar()
    try:
        if conn is not None:
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM empleado")
            empleados_encontrados=cursor.fetchall()
            empleados=[]
            if len(empleados_encontrados)>0:
                for empleado in empleados_encontrados:
                    empleado_encontrado=Empleado(empleado[1],empleado[2],empleado[3],empleado[4],empleado[5])
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
 
def mostrar_empleados():
    conn=conectar()
    try:
        if conn is not None:
            cursor=conn.cursor()
            cursor.execute("SELECT id_empleado, nombre, apellido, direccion, telefono, email, fecha_inicio_contrato, salario FROM empleado")
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

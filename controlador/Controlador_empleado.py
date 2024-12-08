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
            cursor.execute("UPDATE empleado SET nombre=%s, apellido=%s, direccion=%s, telefono=%s, email=%s, fecha_inicio_contrato=%s, salario=%s WHERE id=%s",
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
            cursor.execute("DELETE FROM empleado WHERE id=%s",
                        (empleado.get_id(),))
            conn.commit()
            print("Empleado eliminado")
    except Exception as e:
        print(f"No se eliminaron registros {e}")
    finally:
        cursor.close()
        conn.close()

def buscar_empleado_nombre(nombre):
    conn=conectar()
    try:
        if conn is not None:
            cursor=conn.cursor()
            cursor.execute(
                "SELECT * FROM empleado WHERE nombre=%s",
                (nombre,))
            empleado = cursor.fetchone()
            if empleado  is not None:
                empleado_encontrado=Empleado(empleado [1],empleado [2],empleado [3],empleado [4],empleado [5])
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

def buscar_empleado_id(id):
    conn=conectar()
    try:
        if conn is not None:
            cursor=conn.cursor()
            cursor.execute(
                "SELECT * FROM empleado WHERE id=%s",
                (id,)
                )
            empleado=cursor.fetchone()
            if empleado is not None:
                empleado_encontrado=Empleado(empleado[1],empleado[2],empleado[3],empleado[4],empleado[5])
                empleado_encontrado.set_id(empleado[0])
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

def buscar_empleado_email(email):
    conn=conectar()
    try:
        if conn is not None:
            cursor=conn.cursor()
            cursor.execute(
                "SELECT * FROM empleado WHERE email=%s",
                (email,)
                )
            empleado=cursor.fetchone()
            if empleado is not None:
                empleado_encontrado=Empleado(empleado[1],empleado[2],empleado[3],empleado[4],empleado[5])
                empleado_encontrado.set_id(empleado[0])
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

def registrar_tiempo(id_empleado, id_proyecto, fecha, horas_trabajadas, descripcion_tarea):
    conn = conectar()  # Método para establecer conexión a la base de datos
    try:
        if conn is not None:
            cursor = conn.cursor()
            # Insertar el registro en la base de datos
            cursor.execute("""
                INSERT INTO registro_tiempo (id_empleado, id_proyecto, fecha, horas_trabajadas, descripcion_tarea)
                VALUES (%s, %s, %s, %s, %s)
            """, (id_empleado, id_proyecto, fecha, horas_trabajadas, descripcion_tarea))
            conn.commit()
            print("Registro de tiempo agregado exitosamente.")
    except Exception as e:
        print(f"Error al registrar el tiempo: {e}")
    finally:
        cursor.close()
        conn.close()

def mostrar_registro_tiempo(id_empleado):
    conn = conectar()
    try:
        if conn is not None:
            cursor = conn.cursor()
            # Consulta para obtener los registros de tiempo del empleado
            cursor.execute("""
                SELECT id_registro, id_empleado, id_proyecto, fecha, horas_trabajadas, descripcion_tarea
                FROM registro_tiempo
                WHERE id_empleado = %s
            """, (id_empleado,))
            registros = cursor.fetchall()
            if len(registros) > 0:
                print(f"Registros de tiempo para el empleado con ID {id_empleado}:")
                for registro in registros:
                    print(f"""
                        ID Registro: {registro[0]}
                        ID Empleado: {registro[1]}
                        ID Proyecto: {registro[2]}
                        Fecha: {registro[3]}
                        Horas Trabajadas: {registro[4]}
                        Descripción: {registro[5]}
                    """)
            else:
                print(f"No se encontraron registros de tiempo para el empleado con ID {id_empleado}.")
    except Exception as e:
        print(f"Error al consultar los registros de tiempo: {e}")
    finally:
        cursor.close()
        conn.close()

   
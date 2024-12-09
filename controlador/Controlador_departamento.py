from modelo.ConexionBD import conectar
from modelo.Departamento import Departamento


def agregar_departamento(departamento):
    conn=conectar()
    try:
        if conn is not None:
            cursor=conn.cursor()
            cursor.execute("INSERT INTO departamento (nombre, gerente) VALUES (%s,%s)",
                        (departamento.get_nombre(),departamento.get_gerente()))
            conn.commit()
            print("Dpartamento ingresado")
    except Exception as e:
        print(f"No se agregaron registros {e}")
    finally:
        cursor.close()
        conn.close()

def editar_departamento(departamento):
    conn = conectar()  # Método para establecer conexión a la base de datos
    try:
        if conn is not None:
            cursor = conn.cursor()
            # Actualizar los datos del departamento
            cursor.execute(
                "UPDATE departamento SET nombre = %s, gerente = %s WHERE nombre = %s",
                (departamento.get_nombre(), departamento.get_gerente(), departamento.get_nombre())
            )
            conn.commit()
    except Exception as e:
        print(f"Error al actualizar el departamento: {e}")
    finally:
        cursor.close()
        conn.close()

def buscar_departamento(nombre):
    conn=conectar()
    try:
        if conn is not None:
            cursor=conn.cursor()
            cursor.execute(
                "SELECT id_departamento,nombre,gerente FROM departamento WHERE nombre=%s",
                (nombre,))
            departamento=cursor.fetchone()
            if departamento is not None:
                departamento_encontrado=Departamento(departamento[1],departamento[2])
                departamento_encontrado.set_id(departamento[0])
            else:
                departamento_encontrado=None
            return departamento_encontrado
        else:
            return None
    except Exception as e:
        print(f"Error al conectar. {e}")
    finally:
        cursor.close()
        conn.close()

def eliminar_departamento(departamento):
    conn=conectar()
    try:
        if conn is not None:
            cursor=conn.cursor()
            cursor.execute("DELETE FROM departamento WHERE nombre = %s", (departamento.get_nombre(),))
            conn.commit()
            print("Departamento Eliminado")
    except Exception as e:
        print(f"no se eliminaron registros {e}")
    finally:
        cursor.close()
        conn.close()

def mostrar_departamentos():
    conn = conectar()  # Método para establecer conexión a la base de datos
    try:
        if conn is not None:
            cursor = conn.cursor()
            cursor.execute("SELECT id_departamento, nombre, gerente FROM departamento")
            departamentos = cursor.fetchall()  # Recupera todos los registros

            if departamentos:
                for departamento in departamentos:
                    print(f"ID: {departamento[0]}, Nombre: {departamento[1]}, Gerente: {departamento[2]}")
            else:
                print("No hay departamentos registrados.")
    except Exception as e:
        print(f"Error al mostrar departamentos: {e}")
    finally:
        cursor.close()
        conn.close()
def asignar_empleado_a_departamento(id_empleado, id_departamento):
    conn = conectar()
    try:
        if conn is not None:
            cursor = conn.cursor()
            # Verificar si el empleado ya está asignado a un departamento
            cursor.execute("""
                SELECT id_departamento FROM empleado WHERE id_empleado = %s
            """, (id_empleado,))
            resultado = cursor.fetchone()
            
            if resultado is None:
                print(f"Empleado con ID {id_empleado} no encontrado.")
                return

            # Asignar o actualizar departamento
            cursor.execute("""
                UPDATE empleado
                SET id_departamento = %s
                WHERE id_empleado = %s
            """, (id_departamento, id_empleado))
            conn.commit()
            print(f"Empleado {id_empleado} asignado al departamento {id_departamento}.")
    except Exception as e:
        print(f"Error al asignar empleado al departamento: {e}")
    finally:
        cursor.close()
        conn.close()

def reasignar_empleado_a_departamento(id_empleado, nuevo_id_departamento):
    conn = conectar()
    try:
        if conn is not None:
            cursor = conn.cursor()
            # Verificar si el empleado existe
            cursor.execute("""
                SELECT id_departamento FROM empleado WHERE id_empleado = %s
            """, (id_empleado,))
            resultado = cursor.fetchone()
            
            if resultado is None:
                print(f"Empleado con ID {id_empleado} no encontrado.")
                return
            # Actualizar con el nuevo departamento
            cursor.execute("""
                UPDATE empleado
                SET id_departamento = %s
                WHERE id_empleado = %s
            """, (nuevo_id_departamento, id_empleado))
            conn.commit()
            print(f"Empleado {id_empleado} reasignado al departamento {nuevo_id_departamento}.")
    except Exception as e:
        print(f"Error al reasignar empleado al departamento: {e}")
    finally:
        cursor.close()
        conn.close()
def obtener_empleados_por_departamento(id_departamento):
    conn = conectar()  # Método para establecer conexión a la base de datos
    try:
        if conn is not None:
            cursor = conn.cursor()
            # Consulta para obtener los empleados del departamento
            cursor.execute("""
                SELECT e.id_empleado, e.nombre
                FROM empleado e
                INNER JOIN departamento_empleado de ON e.id_empleado = de.id_empleado
                WHERE de.id_departamento = %s
            """, (id_departamento,))
            return cursor.fetchall()  # Retorna una lista de tuplas con los datos de los empleados
    except Exception as e:
        print(f"Error al obtener empleados por departamento: {e}")
        return []
    finally:
        cursor.close()
        conn.close()
        
def actualizar_departamento(departamento):
    conn = conectar()
    try:
        if conn is not None:
            cursor = conn.cursor()
            cursor.execute("UPDATE departamento SET nombre=%s, gerente=%s WHERE id_departamento=%s",
                           (departamento.get_nombre(),
                            departamento.get_gerente(),
                            departamento.get_id()))
            conn.commit()
            print("Departamento actualizado")
    except Exception as e:
        print(f"No se actualizaron registros: {e}")
    finally:
        cursor.close()
        conn.close()
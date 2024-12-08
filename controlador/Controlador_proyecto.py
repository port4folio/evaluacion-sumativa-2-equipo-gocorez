from modelo.ConexionBD import conectar
from modelo.Proyecto import Proyecto


def agregar_proyecto(proyecto):
    conn = conectar()  # Método para establecer conexión a la base de datos
    try:
        if conn is not None:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO proyecto (nombre, descripcion, fecha_inicio) VALUES (%s, %s, %s)",
                (proyecto.get_nombre(), proyecto.get_descripcion(), proyecto.get_fecha_inicio())
            )
            conn.commit()
            print("Proyecto ingresado exitosamente.")
    except Exception as e:
        print(f"No se agregaron registros: {e}")
    finally:
        cursor.close()
        conn.close()

def editar_proyecto(proyecto):
    conn = conectar()  # Método para establecer conexión a la base de datos
    try:
        if conn is not None:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE proyecto SET nombre = %s, descripcion = %s, fecha_inicio = %s WHERE id = %s",
                (proyecto.get_nombre(), proyecto.get_descripcion(), proyecto.get_fecha_inicio(), proyecto.get_id())
            )
            conn.commit()
            print("Proyecto actualizado exitosamente.")
    except Exception as e:
        print(f"Error al actualizar el proyecto: {e}")
    finally:
        cursor.close()
        conn.close()

def buscar_proyecto(nombre):
    conn = conectar()
    try:
        if conn is not None:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, nombre, descripcion, fecha_inicio FROM proyecto WHERE nombre = %s",
                (nombre,)
            )
            proyecto = cursor.fetchone()
            if proyecto is not None:
                proyecto_encontrado = Proyecto(proyecto[1], proyecto[2], proyecto[3])  # Asumiendo que Proyecto tiene un constructor adecuado
                proyecto_encontrado.set_id(proyecto[0])  # Asumiendo que tienes un método set_id
                return proyecto_encontrado
            else:
                return None
    except Exception as e:
        print(f"Error al buscar el proyecto: {e}")
    finally:
        cursor.close()
        conn.close()

def eliminar_proyecto(proyecto):
    conn = conectar()
    try:
        if conn is not None:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM proyecto WHERE id = %s", (proyecto.get_id(),))
            conn.commit()
            print("Proyecto eliminado exitosamente.")
    except Exception as e:
        print(f"No se eliminaron registros: {e}")
    finally:
        cursor.close()
        conn.close()

def mostrar_proyectos():
    conn = conectar()  # Método para establecer conexión a la base de datos
    try:
        if conn is not None:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nombre, descripcion, fecha_inicio FROM proyecto")
            proyectos = cursor.fetchall()  # Recupera todos los registros

            if proyectos:
                for proyecto in proyectos:
                    print(f"ID: {proyecto[0]}, Nombre: {proyecto[1]}, Descripción: {proyecto[2]}, Fecha de Inicio: {proyecto[3]}")
            else:
                print("No hay proyectos registrados.")
    except Exception as e:
        print(f"Error al mostrar proyectos: {e}")
    finally:
        cursor.close()
        conn.close()

def asignar_proyecto(empleado_id, proyecto_id):
    conn = conectar()  # Método para establecer conexión a la base de datos
    try:
        if conn is not None:
            cursor = conn.cursor()
            # Insertar la asignación en la tabla intermedia empleado_proyecto
            cursor.execute("""
                INSERT INTO empleado_proyecto (empleado_id, proyecto_id)
                VALUES (%s, %s)
            """, (empleado_id, proyecto_id))
            conn.commit()
            print("Proyecto asignado exitosamente.")
    except Exception as e:
        print(f"Error al asignar el proyecto: {e}")
    finally:
        cursor.close()
        conn.close()

def desvincular_proyecto(empleado_id, proyecto_id):
    conn = conectar()  # Método para establecer conexión a la base de datos
    try:
        if conn is not None:
            cursor = conn.cursor()
            # Eliminar la asignación en la tabla intermedia empleado_proyecto
            cursor.execute("""
                DELETE FROM empleado_proyecto
                WHERE empleado_id = %s AND proyecto_id = %s
            """, (empleado_id, proyecto_id))
            conn.commit()
            print("Proyecto desvinculado exitosamente.")
    except Exception as e:
        print(f"Error al desvincular el proyecto: {e}")
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
            cursor = conn.cursor
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

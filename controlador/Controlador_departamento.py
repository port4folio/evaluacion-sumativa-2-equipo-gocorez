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
            print("Departamento actualizado exitosamente.")
    except Exception as e:
        print(f"Error al actualizar el departamento: {e}")
    finally:
        cursor.close()
        conn.close()


def buscar_departamento():
    pass

def eliminar_departamento(departamento):
    conn=conectar()
    try:
        if conn is not None:
            cursor=conn.cursor()
            cursor.execute("DELETE FROM departamento WHERE nombre = %s",(departamento.get_nombre()))
            conn.commit()
            print("Departamento Eliminado")
    except Exception as e:
        print(f"no se eliminaron registros {e}")
    finally:
        cursor.close()
        conn.close()

def mostrar_departamentos():
    pass

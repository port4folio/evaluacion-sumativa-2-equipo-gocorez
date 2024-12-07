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


def buscar_departamento(nombre):
    conn=conectar()
    try:
        if conn is not None:
            cursor=conn.cursor()
            cursor.execute(
                "SELECT id,nombre,gerente FROM departamento WHERE nombre=%s",
                (nombre,)
                )
            departamento=cursor.fetchone()
            if departamento is not None:
                departemento_encontrado=Departamento(departamento[1],departamento[2],departamento[3])
                departemento_encontrado.set_id(departamento[0])
            else:
                departemento_encontrado=None
            return departemento_encontrado
        else:
            return None
    except Exception as e:
        print(f"Error al conectar. {e}")
    finally:
        cursor.close()
        conn.close()

def eliminar_departamento():
    pass

def mostrar_departamentos():
    conn = conectar()  # Método para establecer conexión a la base de datos
    try:
        if conn is not None:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nombre, gerente FROM departamento")
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

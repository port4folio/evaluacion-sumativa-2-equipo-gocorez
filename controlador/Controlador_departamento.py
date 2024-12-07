from modelo.ConexionBD import conectar
from modelo.Departamento import Departamento

def agregar_departamento():
    pass


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

def eliminar_departamento():
    pass

def mostrar_departamentos():
    pass

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

def editar_departamento():
    pass

def buscar_departamento():
    pass

def eliminar_departamento():
    pass

def mostrar_departamentos():
    pass

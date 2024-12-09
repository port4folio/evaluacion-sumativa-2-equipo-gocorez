from modelo.ConexionBD import conectar
import bcrypt
from modelo.Usuario import Usuario

def agregar_usuario(usuario):
    conn=conectar()
    if conn is not None:
        try:
            cursor=conn.cursor()
            pwd_hash=bcrypt.hashpw(usuario.get_passwd().encode('utf-8'),bcrypt.gensalt())
            cursor.execute("INSERT INTO usuario(nombre,edad,passwd,perfil) VALUES(%s,%s,%s,%s)",
                           (usuario.get_nombre(),usuario.get_edad(),pwd_hash,usuario.get_perfil()))
            conn.commit()
            print("Usuario agregado")
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

def buscar_user(nombre):
    conn=conectar()
    try:
        if conn is not None:
            cursor=conn.cursor()
            cursor.execute(
                "SELECT * FROM usuario WHERE nombre=%s",
                (nombre,))
            usuario = cursor.fetchone()
            if usuario  is not None:
                usuario_encontrado=Usuario(usuario [1],usuario [2],usuario [3],usuario [4])
                usuario_encontrado.set_id(usuario [0])
            else:
                usuario_encontrado=None
            return usuario_encontrado
        else:
            return None
    except Exception as e:
        print(f"Error al conectar. {e}")
    finally:
        cursor.close()
        conn.close()
def mostrar_usuarios():#mostrar todos los usuarios
    conn=conectar()
    if conn is not None:
        try:
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM usuario")
            usuarios=cursor.fetchall()
            return usuarios
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

def obtener_usuarios():
    conn=conectar()
    try:
        if conn is not None:
            cursor=conn.cursor()
            cursor.execute("SELECT nombre,edad,passwd,perfil FROM usuario")
            usuarios_encontrados=cursor.fetchall()
            usuarios=[]
            if len (usuarios_encontrados)>0:
                    for usuario in usuarios_encontrados:
                        usuario_encontrado=Usuario(usuario[1],usuario[2],usuario[3],usuario[4])
                        usuario_encontrado.set_id(usuario[0])
                    return usuarios
            else:
                return None
        else:
            return None
    except Exception as e:
        print(f"Error al conectar.{e}")
    finally:
        cursor.close()
        conn.close()

def eliminar_usuario(usuario):
    conn=conectar()
    try:
        if conn is not None:
            cursor=conn.cursor()
            cursor.execute("DELETE FROM usuario WHERE id=%s",(usuario.get_id(),))
            conn.commit()
            print("usuario eliminado")
    except Exception as e:
        print(f"no se eliminaron registros {e}")
    finally:
        cursor.close()
        conn.close()

def actualizar_usuario(usuario):### Editar Usuario
    conn=conectar()
    try:
        if conn is not None:
            cursor=conn.cursor()
            cursor.execute("UPDATE usuario SET nombre=%s,edad=%s,passwd=%s,perfil=%s WHERE id=%s",
                           (usuario.get_nombre(),usuario.get_edad(),usuario.get_passwd(),usuario.get_perfil(),usuario.get_id()))
            conn.commit()
        print("usuario actualizado")
    except Exception as e:
        print(f"No se agregaron registros {e}")
    finally:
        cursor.close()
        conn.close()


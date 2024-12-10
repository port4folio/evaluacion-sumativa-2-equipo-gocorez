from Controlador_usuario import mostrar_usuarios,buscar_user
import bcrypt
def hay_usuarios():
    if len(mostrar_usuarios())>0:
        return True
    else:
        return False

def autenticar(nombre,passwd):
    usuario=buscar_user(nombre)
    if usuario is not None:
        if bcrypt.checkpw(passwd.encode('utf-8'),usuario[3].encode('utf-8')):
            return usuario
    return None
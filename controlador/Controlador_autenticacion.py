from .Controlador_usuario import mostrar_usuarios,buscar_user
import bcrypt
def hay_usuarios():
    usuarios = mostrar_usuarios()
    if usuarios is None:
        return False
    return len(usuarios) > 0

def autenticar(nombre,passwd):
    usuario=buscar_user(nombre)
    if usuario is not None:
        if bcrypt.checkpw(passwd.encode('utf-8'),usuario.get_passwd().encode('utf-8')):
            return usuario
    return None
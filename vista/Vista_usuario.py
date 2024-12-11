from modelo.Usuario import Usuario
from controlador.Controlador_usuario import agregar_usuario,buscar_user,actualizar_usuario,eliminar_usuario,mostrar_usuarios

def leer_numero(mensaje):
    while True:
        try:
            op=int(input(mensaje))
            return op
        except:
            print("Debe ingresar un número.")

def menu():
    print("App Usuarios")
    print("1.- Agregar")
    print("2.- Editar")#pendiente 
    print("3.- Eliminar")#
    print("4.- Mostrar uno")
    print("5.- Mostrar todos")
    print("0.- Salir")
    op=leer_numero("Ingrese una opción: ")
    return op

def add_user():#Agregar Usuario 
    print("====Registro de Usuario====")
    nombre=input("Ingrese nombre: ")
    edad=leer_numero("Ingrese edad: ")
    passwd=input("Ingrese contraseña: ")
    perfil=input("Ingrese perfil de usuario: ")
    usuario=Usuario(nombre,edad,passwd,perfil)
    agregar_usuario(usuario)

def edit_user():#Editar Usuario
    print("===Editar usuario===")
    try:
        nombre_usuario=input("Ingrese nombre del usuario a editar: ")
        usuario=buscar_user(nombre_usuario)
        if not usuario:
            print("No existe el usuario")
            return
        print(f"Usuario encontrado: id: {usuario.get_id()}, Nombre: {usuario.get_nombre()},Edad: {usuario.get_edad()},Passwd: {usuario.get_passwd()},Perfil: {usuario.get_perfil()}")
        nuevo_nombre=input("Ingrese su nuevo nombre (presione Enter para mantener el actual): ")
        nuevo_edad=leer_numero("Ingrese su nueva edad (presione Enter para mantener el actual): ")
        nuevo_passwd=input("Ingrese su nueva contraseña (presione Enter para mantener la actual): ")
        nuevo_perfil=input("Ingrese su nuevo perfil (presione Enter para mantener el actual): ")
        if nuevo_nombre:
            usuario.set_nombre(nuevo_nombre)
        if nuevo_edad:
            usuario.set_edad(nuevo_edad)
        if nuevo_passwd:
            usuario.set_passwd(nuevo_passwd)
        if nuevo_perfil:
            usuario.set_perfil(nuevo_perfil)
        actualizar_usuario(usuario)
    except ValueError:
        print("Error: Por favor ingrese valores válidos.")
    except Exception as e:
        print(f"Error al editar usuario: {e}")

def delete_usuario():
    print("===Eliminar usuario===")
    nombre=input("Ingrese nombre del usuario a eliminar: ")
    usuario=buscar_user(nombre)
    if usuario is not None:
        print("Usuario encontrado: ")
        print(f"Nombre: {usuario.get_nombre()}")
        print(f"Edad: {usuario.get_edad()}")
        print(f"Passwd: {usuario.get_passwd()}")
        print(f"Perfil: {usuario.get_perfil()}")
        confirmacion=input("¿Desea eliminar el usuario? (s/n): ")
        if confirmacion.lower() == "s":
            eliminar_usuario(usuario)
        else:
            print("Operación cancelada")
    else:
        print("Usuario no encontrado ")

def view_usuario():
    nombre=input("Ingrese nombre del usuario a buscar: ")
    usuario=buscar_user(nombre)
    print(usuario)

def view_usuarios():
    usuarios=mostrar_usuarios()
    if len(usuarios)>0:
        for usuario in usuarios:
            print(usuario)
    else:
        print("No hay usuarios ingresados")

def main_usuario():
    while True:
        op=menu()
        if op==1:#agregar
            add_user()
        elif op==2:#editar
            edit_user()
        elif op==3:#eliminar
            delete_usuario()
        elif op==4:
            view_usuario()
        elif op==5:
            view_usuarios()
        elif op==0:
            print("Gracias por preferirnos")
            break

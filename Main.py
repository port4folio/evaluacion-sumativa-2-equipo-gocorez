from vista.Vista_menu import menu_principal
from controlador.Controlador_autenticacion import hay_usuarios,autenticar
from vista.Vista_usuario import add_user


while True:
    print("hola")
    if hay_usuarios():
        print("Inicio sesión")
        nombre=input("Ingrese nombre: ")
        passwd=input("Ingrese contraseña: ")
        usuario=autenticar(nombre,passwd)
        if usuario is not None:
            print(f"Bienvenido {usuario[1]}")
            menu_principal()
            break
        else:
            print("Usuario o contraseña incorrecta.")
    else:
        add_user()


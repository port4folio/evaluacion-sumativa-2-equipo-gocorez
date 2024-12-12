from vista.Vista_menu import iniciar_menu
from controlador.Controlador_autenticacion import hay_usuarios, autenticar
from vista.Vista_usuario import add_user

while True:
    if hay_usuarios():
        print("Inicio sesión")
        nombre = input("Ingrese nombre: ")
        passwd = input("Ingrese contraseña: ")
        usuario = autenticar(nombre, passwd)
        if usuario is not None:
            print(f"Bienvenido {usuario.get_nombre()}")
            iniciar_menu(usuario)  # Llama a la función iniciar_menu del archivo Vista_menu.py
            break
        else:
            print("Usuario o contraseña incorrecta.")
    else:
        add_user()

# Libreria parea conectar con la base de datos
# pip install mysql-connector-python

# Para crear un archivo con el listado de librerias de mi proyecto
# pip freeze > requirements.txt

import mysql.connector
from mysql.connector import Error

def conectar():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            database="ecotech solutions",
            user = "usuario_ecotech",
            password = "user_ecotech"
        )
        return conn
    except Error as e :
        print(f"No se pudo conectar a la base de datos {e}")
        return None


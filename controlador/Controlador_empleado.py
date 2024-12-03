from modelo.ConexionBD import conectar
from modelo.Empleado import Empleado

def generar_email_unico(nombre, apellido):
    base_email = f"{nombre.lower()}.{apellido.lower()}@ecotech.com"
    email = base_email
    contador = 1

    conn = conectar()
    try:
        cursor = conn.cursor()
        while email_existe(cursor, email):
            email = f"{base_email.split('@')[0]}{contador}@ecotech.com"
            contador += 1
    finally:
        cursor.close()
        conn.close()
    
    return email

def email_existe(cursor, email):
    cursor.execute("SELECT COUNT(*) FROM empleado WHERE email = %s", (email,))
    return cursor.fetchone()[0] > 0

def agregar_empleado(empleado):
    conn = conectar()
    try:
        if conn is not None:
            cursor = conn.cursor()
            # Generar el email único
            email = generar_email_unico(empleado.get_nombre(), empleado.get_apellido())
            # Actualizar el email en el objeto empleado
            empleado.set_email(email)

            cursor.execute("INSERT INTO empleado (nombre, apellido, direccion, telefono, email, fecha_inicio_contrato, salario) VALUES (%s, %s, %s, %s, %s, %s,%s)",
                           (empleado.get_nombre(), 
                            empleado.get_apellido(),
                            empleado.get_direccion(),
                            empleado.get_telefono(), 
                            empleado.get_email(), 
                            empleado.get_fecha_inicio_contrato(), 
                            empleado.get_salario()))
            conn.commit()
            print("Empleado ingresado con éxito")
    except Exception as e:
        print(f"Error al agregar empleado: {e}")
    finally:
        cursor.close()
        conn.close()

def actualizar_empleado():
    pass

def borrar_empleado():
    pass


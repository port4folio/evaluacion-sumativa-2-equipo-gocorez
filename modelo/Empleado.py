class Empleado:

    # Constructor
    def __init__(self, nombre, apellido, direccion, telefono, email, fecha_inicio_contrato, salario):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__direccion = direccion
        self.__telefono = telefono
        self.__email = email
        self.__fecha_inicio_contrato = fecha_inicio_contrato
        self.__salario = salario
        self.__id = 0
   

    # Getters
    def get_nombre(self):
        return self.__nombre
    
    def get_apellido(self):
        return self.__apellido

    def get_direccion(self):
        return self.__direccion

    def get_telefono(self):
        return self.__telefono

    def get_email(self):
        return self.__email

    def get_fecha_inicio_contrato(self):
        return self.__fecha_inicio_contrato

    def get_salario(self):
        return self.__salario
    
    def get_id(self):
        return self.__id

    # Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_apellido(self, apellido):  
        self.__apellido = apellido  

    def set_direccion(self, direccion):
        self.__direccion = direccion

    def set_telefono(self, telefono):
        self.__telefono = telefono

    def set_email(self, email):
        self.__email = email

    def set_fecha_inicio_contrato(self, fecha_inicio_contrato):
        self.__fecha_inicio_contrato = fecha_inicio_contrato

    def set_salario(self, salario):
        self.__salario = salario

    def set_id(self, id):
        self.__id = id
        
    # ToString
    def __str__(self):
        return f"Nombre:{self.__nombre}\nApellido:{self.__apellido}\nDirección:{self.__direccion}\nTeléfono:{self.__telefono}\nEmail:{self.__email}\nFecha de inicio contrato:{self.__fecha_inicio_contrato}\nSalario:{self.__salario}"    
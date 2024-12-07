class Proyecto:
    
    def __init__(self, nombre,descrpcion, fecha_inicio):
        self.__nombre = nombre
        self.__descripcion = descrpcion
        self.__fecha_inicio = fecha_inicio

# Getters
    def get_nombre(self):
        return self.__nombre
    
    def get_descripcion(self):
        return self.__descripcion
    
    def get_fecha_inicio(self):
        return self.__fecha_inicio
    
# Setters 
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_descripcion(self, descripcion):
        self.__descripcion = descripcion

    def set_fecha_inicio(self, fecha_inicio ):
        self.__fecha_inicio = fecha_inicio

        
# Mostrar datos
    def __str__(self):
        return f"Nombre: {self.__nombre}, Descripcion: {self.__descripcion}, Fecha de inicio: {self.__fecha_inicio}"

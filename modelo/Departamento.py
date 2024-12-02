class Departamento:

    # Constructor
    def __init__(self, nombre, gerente):
        self.__nombre = nombre
        self.__gerente = gerente

    #Getters
    def get_nombre(self):
        return self.__nombre
    
    def get_gerente(self):
        return self.__gerente
    
    #Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_gerente(self, gerente):
        self.__gerente = gerente    

    #Mostrar datos 
    def __str__(self):
        return f"Nombre:{self.__nombre}\nGerente: {self.__gerente}"   
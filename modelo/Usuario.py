class Usuario:
    def __init__(self,nombre,edad,passwd,perfil):
        self.__nombre=nombre
        self.__edad=edad
        self.__passwd=passwd
        self.__perfil=perfil
        self.__id=0


    def get_perfil(self):
        return self.__perfil
    
    def set_perfil(self,perfil):
        self.__perfil=perfil

    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self,nombre):
        self.__nombre=nombre

    def get_edad(self):
        return self.__edad
    
    def set_edad(self, edad):
        self.__edad = edad

    def get_passwd(self):
        return self.__passwd    

    def set_passwd(self, passwd):
        self.__passwd = passwd
    
    def get_id(self):
        return self.__id
    
    def set_id(self,id):
        self.__id=id

    def __str__(self):
        return f"Nombre: {self.__nombre}\nEdad: {self.__edad}\nPerfil: {self.__perfil}"

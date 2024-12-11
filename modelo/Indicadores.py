class Indicadores:
    def __init__(self, nombre_indicador,fecha_indicador, fecha_consulta,usuario_consulta,sitio_consulta):
        self.__nombre_indicador = nombre_indicador
        self.__fecha_indicador = fecha_indicador
        self.__fecha_consulta = fecha_consulta
        self.__usuario_consulta = usuario_consulta
        self.__sitio_consulta = sitio_consulta
        self.__id = 0 

#Getters
    def get_nombre_indicador(self):
        return self.__nombre_indicador
    
    def get_fecha_indicador(self):
        return self.__fecha_indicador
    
    def get_fecha_consulta(self):
        return self.__fecha_consulta
    
    def get_usuario_consulta(self):
        return self.__usuario_consulta
    
    def get_sitio_consulta(self):
        return self.__sitio_consulta
    
    def get_id(self):
        return self.__id
    
#Setters
    def set_nombre_indicador(self, nombre_indicador):
        self.__nombre_indicador = nombre_indicador

    def set_fecha_indicador(self, fecha_indicador):
        self.__fecha_indicador = fecha_indicador

    def set_fecha_consulta(self, fecha_consulta):
        self.__fecha_consulta = fecha_consulta

    def set_usuario_consulta(self, usuario_consulta):
        self.__usuario_consulta = usuario_consulta

    def set_sitio_consulta(self, sitio_consulta):
        self.__sitio_consulta = sitio_consulta

    def set_id(self, id):
        self.__id = id

 # Mostrar datos 
    def __str__(self):
        return f"Nombre Indicador: {self.__nombre_indicador}\nFecha Indicador: {self.__fecha_indicador}\nFecha consulta: {self.__fecha_consulta}\n Usuario consulta: {self.__usuario_consulta}\nSitio consulta: {self.__sitio_consulta}"


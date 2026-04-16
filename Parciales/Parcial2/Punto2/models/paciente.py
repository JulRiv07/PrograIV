class Paciente:
    def __init__(self, documento: int, nombre: str, edad: int, estadoDeAtencion: str):
        self.__documento = documento
        self.__nombre = nombre
        self.__edad = edad
        self.__estadoDeAtencion = estadoDeAtencion

    @property
    def documento(self):
        return self.__documento
    @documento.setter
    def documento(self, documento: int):
        self.__documento = documento

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad(self, edad: int):
        self.__edad = edad

    @property
    def estadoDeAtencion(self):
        return self.__estadoDeAtencion
    @estadoDeAtencion.setter
    def estadoDeAtencion(self, estadoDeAtencion: str):
        self.__estadoDeAtencion = estadoDeAtencion

    def __str__(self):
        return (f"Documento: {self.__documento}, Nombre: {self.__nombre}, "
                f"Edad: {self.__edad}, Estado de atención: {self.__estadoDeAtencion}")
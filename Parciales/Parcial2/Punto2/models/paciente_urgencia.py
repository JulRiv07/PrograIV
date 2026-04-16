from models.paciente import Paciente

class PacienteUrgencia(Paciente):
    def __init__(self, documento: int, nombre: str, edad: int, estadoDeAtencion: str, nivelDeGravedad: str):
        super().__init__(documento, nombre, edad, estadoDeAtencion)
        self.__nivelDeGravedad = nivelDeGravedad

    @property
    def nivelDeGravedad(self):
        return self.__nivelDeGravedad
    @nivelDeGravedad.setter
    def nivelDeGravedad(self, nivelDeGravedad: str):
        self.__nivelDeGravedad = nivelDeGravedad

    def __str__(self):
        return super().__str__() + f", Nivel de gravedad: {self.__nivelDeGravedad}"
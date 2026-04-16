from models.paciente import Paciente

class PacientePrioritario(Paciente):
    def __init__(self, documento: int, nombre: str, edad: int, estadoDeAtencion: str, condicionEspecial: str):
        super().__init__(documento, nombre, edad, estadoDeAtencion)
        self.__condicionEspecial = condicionEspecial

    @property
    def condicionEspecial(self):
        return self.__condicionEspecial
    @condicionEspecial.setter
    def condicionEspecial(self, condicionEspecial: str):
        self.__condicionEspecial = condicionEspecial

    def __str__(self):
        return super().__str__() + f", Condición especial: {self.__condicionEspecial}"
from Parcial2.Punto2.models.paciente import Paciente

class PacienteGeneral(Paciente):
    def __init__(self, documento: int, nombre: str, edad: int, estadoDeAtencion: str, nombreEps: str):
        super().__init__(documento, nombre, edad, estadoDeAtencion)
        self.__nombreEps = nombreEps

    @property
    def nombreEps(self):
        return self.__nombreEps
    @nombreEps.setter
    def nombreEps(self, nombreEps: str):
        self.__nombreEps = nombreEps

    def __str__(self):
        return super().__str__() + f", Nombre de la EPS: {self.__nombreEps}"
class Vehiculo:
    def __init__(self, placa: str, marca: str, modelo: str, precioPorDia: float, disponible: bool = True):
        self.__placa = placa.upper()
        self.__marca = marca
        self.__modelo = modelo
        self.__precioPorDia = precioPorDia
        self.__disponible = disponible

    @property
    def placa(self):
        return self.__placa

    @placa.setter
    def placa(self, placa: str):
        self.__placa = placa.upper()

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, marca: str):
        self.__marca = marca

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, modelo: str):
        self.__modelo = modelo

    @property
    def precioPorDia(self):
        return self.__precioPorDia

    @precioPorDia.setter
    def precioPorDia(self, precioPorDia: float):
        if precioPorDia < 0:
            raise ValueError("El precio por día no puede ser negativo.")
        self.__precioPorDia = precioPorDia

    @property
    def disponible(self):
        return self.__disponible

    @disponible.setter
    def disponible(self, disponible: bool):
        self.__disponible = disponible

    def toDict(self):
        return {
            "placa"      : self.__placa,
            "marca"      : self.__marca,
            "modelo"     : self.__modelo,
            "precioPorDia": self.__precioPorDia,
            "disponible" : self.__disponible,
        }

    def __str__(self):
        estado = "Disponible" if self.__disponible else "Alquilado"
        return f"Placa: {self.__placa:<10} | Marca: {self.__marca:<12} | Modelo: {self.__modelo:<12} | Precio/día: ${self.__precioPorDia:>10,.0f} | Estado: {estado}"

class Automovil(Vehiculo):
    def __init__(self, placa: str, marca: str, modelo: str, precioPorDia: float, numeroPuertas: int, disponible: bool = True):
        super().__init__(placa, marca, modelo, precioPorDia, disponible)
        self.__numeroPuertas = numeroPuertas

    @property
    def numeroPuertas(self):
        return self.__numeroPuertas

    @numeroPuertas.setter
    def numeroPuertas(self, numeroPuertas: int):
        if numeroPuertas <= 0:
            raise ValueError("El número de puertas debe ser mayor a 0.")
        self.__numeroPuertas = numeroPuertas

    def toDict(self):
        data = super().toDict()
        data["numeroPuertas"] = self.__numeroPuertas
        return data

    def __str__(self):
        return super().__str__() + f" | Puertas: {self.__numeroPuertas}"


class Motocicleta(Vehiculo):
    def __init__(self, placa: str, marca: str, modelo: str, precioPorDia: float, cilindraje: int, disponible: bool = True):
        super().__init__(placa, marca, modelo, precioPorDia, disponible)
        self.__cilindraje = cilindraje

    @property
    def cilindraje(self):
        return self.__cilindraje

    @cilindraje.setter
    def cilindraje(self, cilindraje: int):
        if cilindraje <= 0:
            raise ValueError("El cilindraje debe ser mayor a 0.")
        self.__cilindraje = cilindraje

    def toDict(self):
        data = super().toDict()
        data["cilindraje"] = self.__cilindraje
        return data

    def __str__(self):
        return super().__str__() + f" | Cilindraje: {self.__cilindraje} cc"


class Camion(Vehiculo):
    def __init__(self, placa: str, marca: str, modelo: str, precioPorDia: float, capacidadCarga: int, disponible: bool = True):
        super().__init__(placa, marca, modelo, precioPorDia, disponible)
        self.__capacidadCarga = capacidadCarga

    @property
    def capacidadCarga(self):
        return self.__capacidadCarga

    @capacidadCarga.setter
    def capacidadCarga(self, capacidadCarga: int):
        if capacidadCarga <= 0:
            raise ValueError("La capacidad de carga debe ser mayor a 0.")
        self.__capacidadCarga = capacidadCarga

    def toDict(self):
        data = super().toDict()
        data["capacidadCarga"] = self.__capacidadCarga
        return data

    def __str__(self):
        return super().__str__() + f" | Carga: {self.__capacidadCarga} ton"
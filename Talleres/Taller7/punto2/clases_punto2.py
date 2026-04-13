class Vehiculo2:
    def __init__(self, color, ruedas):
        self.set_color(color)
        self.set_ruedas(ruedas)

    def set_color(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

    def set_ruedas(self, ruedas):
        if ruedas > 0:
            self.__ruedas = ruedas
        else:
            raise ValueError("Ruedas inválidas")

    def get_ruedas(self):
        return self.__ruedas

    def mostrar(self):
        return f"Color: {self.__color}, Ruedas: {self.__ruedas}"


class Coche(Vehiculo2):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.set_velocidad(velocidad)
        self.set_cilindrada(cilindrada)

    def set_velocidad(self, velocidad):
        if velocidad > 0:
            self.__velocidad = velocidad
        else:
            raise ValueError("Velocidad inválida")

    def get_velocidad(self):
        return self.__velocidad

    def set_cilindrada(self, cilindrada):
        if cilindrada > 0:
            self.__cilindrada = cilindrada
        else:
            raise ValueError("Cilindrada inválida")

    def get_cilindrada(self):
        return self.__cilindrada

    def mostrar(self):
        return super().mostrar() + f", Velocidad: {self.__velocidad}, Cilindrada: {self.__cilindrada}"


class Bicicleta(Vehiculo2):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.set_tipo(tipo)

    def set_tipo(self, tipo):
        self.__tipo = tipo

    def get_tipo(self):
        return self.__tipo

    def mostrar(self):
        return super().mostrar() + f", Tipo: {self.__tipo}"


class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.set_carga(carga)

    def set_carga(self, carga):
        if carga >= 0:
            self.__carga = carga
        else:
            raise ValueError("Carga inválida")

    def get_carga(self):
        return self.__carga

    def mostrar(self):
        return super().mostrar() + f", Carga: {self.__carga}"


class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.set_velocidad(velocidad)
        self.set_cilindrada(cilindrada)

    def set_velocidad(self, velocidad):
        if velocidad > 0:
            self.__velocidad = velocidad
        else:
            raise ValueError("Velocidad inválida")

    def set_cilindrada(self, cilindrada):
        if cilindrada > 0:
            self.__cilindrada = cilindrada
        else:
            raise ValueError("Cilindrada inválida")

    def mostrar(self):
        return super().mostrar() + f", Velocidad: {self.__velocidad}, Cilindrada: {self.__cilindrada}"


def catalogar(vehiculos, ruedas=None):
    contador = 0

    for v in vehiculos:
        if ruedas is None or v.get_ruedas() == ruedas:
            print(type(v).__name__, "->", v.mostrar())
            contador += 1

    if ruedas is not None:
        print(f"\nSe encontraron {contador} vehículos con {ruedas} ruedas")
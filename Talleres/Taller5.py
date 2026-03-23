import json
import math

# Clases del primer punto

class Vehiculo:
    def __init__(self, marca, año):
        self.marca = marca
        self.año = año
    
    def duracion_llantas(self):
        if self.marca == "Michelin":
            return "5 Años"
        elif self.marca == "Goodyear":
            return "4 años"
        else:
            return "3 años"
        
    def tipo_combustible(self):
        return "corriente"
    
    def guardar(self):
        datos = self.__dict__
        with open("Vehiculos.txt", "a") as f:
            f.write(json.dumps(datos) + "\n")

class Camion(Vehiculo):
    def tipo_combustible(self):
        return "ACPM"
    
class Moto(Vehiculo):
    def tipo_combustible(self):
        return "Corriente"
    
class Automovil(Vehiculo):
    def tipo_combustible(self):
        return "Extra"
    
    def tiempo_viaje(self, distancia, velocidad = 80):
        return distancia / velocidad
    
    def gasto_mensual(self):
        precio_gasolina = 16800
        consumo_km = 15
        kg_mes = 1000
        return (kg_mes / consumo_km ) * precio_gasolina
    
# Clases del segundo punto

class Vehiculo2:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

class Coche(Vehiculo2):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada


class Bicicleta(Vehiculo2):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo


class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga


class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

def catalogar(vehiculos, ruedas = None):
    contador = 0
    for v in vehiculos:
        if ruedas is None or v.ruedas == ruedas:
            print(type(v).__name__, vars(v))
            contador += 1
    
    if ruedas is not None:
        print(f"Se han encontrado {contador} vehiculos con {ruedas} ruedas")

#  Clases del tercer punto

class Figura:
    def area(self):
        pass

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura
    
class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2
    
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return math.pi * self.radio**2
    
#  Clases del cuarto punto

class Transporte:
    def __init__(self, capacidad, tarifa):
        self.capacidad = capacidad
        self.tarifa = tarifa

    def calcular_pasaje(self, km):
        pass

class Bus(Transporte):
    def calcular_pasaje(self, km):
        return self.tarifa + (100 * km)
    
class Taxi(Transporte):
    def calcular_pasaje(self, km):
        return 500 * km

class Metro(Transporte):
    def calcular_pasaje(self, km):
        return self.tarifa

# Funciones para cada uno de los ejercicios

def punto1():
    print("\n--- Sistema de Vehículos ---")

    v1 = Automovil("Michelin", 2020)
    v2 = Moto("Genérica", 2022)
    v3 = Camion("Goodyear", 2018)

    for v in [v1, v2, v3]:
        print("\nVehículo:", type(v).__name__)
        print("Duración llantas:", v.duracion_llantas())
        print("Combustible:", v.tipo_combustible())

        if isinstance(v, Automovil):
            print("Tiempo viaje (100 km):", v.tiempo_viaje(100))
            print("Gasto mensual:", v.gasto_mensual())

        v.guardar()

def punto2():
    print("\n--- Catálogo ---")

    vehiculos = [
        Coche("Rojo", 4, 180, 2000),
        Bicicleta("Azul", 2, "Urbana"),
        Camioneta("Blanco", 4, 160, 2500, 500),
        Motocicleta("Negro", 2, "Deportiva", 200, 600)
    ]

    print("\nTodos los vehículos:")
    catalogar(vehiculos)

    print("\nFiltrar por ruedas (2):")
    catalogar(vehiculos, 2)

    print("\nFiltrar por ruedas (4):")
    catalogar(vehiculos, 4)

def punto3():
    print("\n--- Figuras ---")

    figuras = [
        Rectangulo(4, 5),
        Triangulo(3, 6),
        Circulo(2)
    ]

    for f in figuras:
        print(type(f).__name__, "Área:", f.area())

def punto4():
    print("\n--- Transporte ---")

    transportes = [
        Bus(40, 2000),
        Taxi(4, 0),
        Metro(200, 3000)
    ]

    for t in transportes:
        print(type(t).__name__, "Costo (10 km):", t.calcular_pasaje(10))

#Menu principal

def main():
    while True:
        print("\nMenú")
        print("1. Sistema de Vehículos (Punto 1)")
        print("2. Catálogo de Vehículos (Punto 2)")
        print("3. Figuras (Punto 3)")
        print("4. Transporte (Punto 4)")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            punto1()
        elif opcion == "2":
            punto2()
        elif opcion == "3":
            punto3()
        elif opcion == "4":
            punto4()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, intente de nuevo")

main()
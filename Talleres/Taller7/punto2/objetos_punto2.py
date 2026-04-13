from .clases_punto2 import Coche, Bicicleta, Camioneta, Motocicleta

def crear_vehiculos():
    return [
        Coche("Rojo", 4, 180, 2000),
        Bicicleta("Azul", 2, "Urbana"),
        Camioneta("Blanco", 4, 160, 2500, 500),
        Motocicleta("Negro", 2, "Deportiva", 200, 600)
    ]
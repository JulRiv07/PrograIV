from Parcial2.Punto3.models.producto import Producto

class Computador(Producto):
    def __init__(self, id, nombre, precio, cantidad, ram, procesador):
        super().__init__(id, nombre, precio, cantidad)
        self.ram = ram
        self.procesador = procesador
    
    def mostrarInfo(self):
        return super().mostrarInfo() + f" | RAM: {self.ram}, CPU: {self.procesador}"
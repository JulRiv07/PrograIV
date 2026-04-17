from Parcial2.Punto3.models.producto import Producto

class Celular(Producto):
    def __init__(self, id, nombre, precio, cantidad, almacenamiento, camaras):
        super().__init__(id, nombre, precio, cantidad)
        self.almacenamiento = almacenamiento
        self.camaras = camaras

    def mostrarInfo(self):
        return super().mostrarInfo() + f" | Almacenamiento: {self.almacenamiento}GB, Cámaras: {self.camaras}"
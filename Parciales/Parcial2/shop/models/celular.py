from models.producto import Producto

class Celular(Producto):
    def __init__(self, id, nombre, precio, cantidad, almacenamiento, camaras):
        super().__init__(id, nombre, precio, cantidad)
        self.almacenamiento = almacenamiento
        self.camaras = camaras

    def mostrar_info(self):
        return super().mostrar_info() + f"| Almacenamiento: {self.almacenamiento}GB, Cámaras: {self.camaras}"
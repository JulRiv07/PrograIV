from models.producto import Producto

class Accesorio(Producto):
    def __init__(self, id, nombre, precio, cantidad, tipo):
        super().__init__(id, nombre, precio, cantidad)
        self.tipo = tipo
    
    def mostrarInfo(self):
        return super().mostrarInfo() + f" | Tipo: {self.tipo}"
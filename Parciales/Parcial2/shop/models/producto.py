class Producto:
    def __init__(self, id, nombre, precio, cantidad):
        self.__id = id
        self.__nombre = nombre
        self.__precio = precio
        self.__cantidad = cantidad
    
    def getId(self):
        return self.__id
    
    def getNombre(self):
        return self.__nombre
    
    def getPrecio(self):      
        return self.__precio
    
    def getCantidad(self):
        return self.__cantidad
    
    def setCantidad(self, cantidad):
        self.__cantidad = cantidad

    def mostrarInfo(self):
        return f"{self.__nombre} - ${self.__precio} - Stock: {self.__cantidad}"
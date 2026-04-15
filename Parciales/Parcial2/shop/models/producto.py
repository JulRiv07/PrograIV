class Producto:
    def __init__(self, id, nombre, precio, cantidad):
        self.__id = id
        self.__nombre = nombre
        self.__precio = precio
        self.__cantidad = cantidad
    
    def get_id(self):
        return self.__id
    
    def get_nombre(self):
        return self.__nombre
    
    def get_precio(self):      
        return self.__precio
    
    def get_cantidad(self):
        return self.__cantidad
    
    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def mostrar_info(self):
        return f"{self.__nombre} - ${self.__precio} - Stock: {self.__cantidad}"
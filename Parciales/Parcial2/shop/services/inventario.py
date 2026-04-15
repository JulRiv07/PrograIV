from services.json import guardar, cargar

class Inventario:
    def __init__(self):
        self.productos = {}
        self.productos = cargar()

    def registrar_producto(self, producto):
        if producto.get_id() in self.productos:
            print("Este producto ya fue registrado.")
            return

        self.productos[producto.get_id()] = producto
        guardar(self.productos)
        print("Producto registrado exitosamente.")

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
            return

        for producto in self.productos.values():
            print(producto.mostrar_info())

    def buscar_producto(self, id):
        return self.productos.get(id, None)
    
    def rebastecer(self, id, cantidad):
        producto = self.buscar_producto(id)
        if producto:
            producto.set_cantidad(producto.get_cantidad() + cantidad)
            print(f"Producto {producto.get_nombre()} rebastecido. Nueva cantidad: {producto.get_cantidad()}")
            guardar(self.productos)
        else:
            print("Producto no encontrado.")

    def consultar_producto(self, id):
        producto = self.buscar_producto(id)
        if producto:
            print(producto.mostrar_info())
        else:
            print("Producto no encontrado.")

    def vender(self, id, cantidad):
        producto = self.buscar_producto(id)
        if not producto:
            print("Producto no encontrado.")
            return

        if cantidad <= 0:
            print("Cantidad inválida.")
            return

        if producto.get_cantidad() < cantidad:
            print("Stock insuficiente.")
            return
        
        subtotal = producto.get_precio() * cantidad
        descuento = 0

        if cantidad >= 3:
            descuento += subtotal * 0.08

        if subtotal >= 500:
            descuento += subtotal * 0.05

        total = subtotal - descuento
        producto.set_cantidad(producto.get_cantidad() - cantidad)
        print(f"Venta exitosa. Subtotal: ${subtotal:.2f} (Descuento: ${descuento:.2f}) \n Total: ${total:.2f}")
        guardar(self.productos)
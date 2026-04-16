from services.json import guardarProductos, cargarProductos

class Inventario:
    def __init__(self):
        self.productos = cargarProductos()
        self.ventasPorCategoria = {} 

    def registrarProducto(self, producto):
        if producto.getId() in self.productos:
            print("Este producto ya fue registrado.")
            return

        self.productos[producto.getId()] = producto
        guardarProductos(self.productos)
        print("Producto registrado exitosamente.")

    def mostrarInventario(self):
        if not self.productos:
            print("El inventario está vacío.")
            return

        for producto in self.productos.values():
            print(producto.mostrarInfo())

    def buscarProducto(self, id):
        return self.productos.get(id, None)
    
    def reabastecer(self, id, cantidad):
        producto = self.buscarProducto(id)
        if producto:
            producto.setCantidad(producto.getCantidad() + cantidad)
            print(f"Producto {producto.getNombre()} actualizado. Stock: {producto.getCantidad()}")
            guardarProductos(self.productos)
        else:
            print("Producto no encontrado.")

    def consultarProducto(self, id):
        producto = self.buscarProducto(id)
        if producto:
            print(producto.mostrarInfo())
        else:
            print("Producto no encontrado.")

    def venderProducto(self, id, cantidad):
        producto = self.buscarProducto(id)
        if not producto:
            print("Producto no encontrado.")
            return
        
        if cantidad <= 0:
            print("Cantidad inválida.")
            return
        
        if producto.getCantidad() < cantidad:
            print("Stock insuficiente.")
            return
        
        subtotal = producto.getPrecio() * cantidad
        descuento = 0

        if cantidad >= 3:
            descuento += subtotal * 0.08
        if subtotal >= 500:
            descuento += subtotal * 0.05

        total = subtotal - descuento
        producto.setCantidad(producto.getCantidad() - cantidad)
        print(f"Venta exitosa. Subtotal: ${subtotal:.2f} (Descuento: ${descuento:.2f}) \nTotal: ${total:.2f}")
        tipo = producto.__class__.__name__

        if tipo in self.ventasPorCategoria:
            self.ventasPorCategoria[tipo] += cantidad
        else:
            self.ventasPorCategoria[tipo] = cantidad

        guardarProductos(self.productos)

    def categoriaMasVendida(self):
        if not self.ventasPorCategoria:
            print("No hay ventas registradas.")
            return

        categoria = max(self.ventasPorCategoria, key=self.ventasPorCategoria.get)
        cantidad = self.ventasPorCategoria[categoria]

        print(f"Categoría más vendida: {categoria} ({cantidad} unidades)")

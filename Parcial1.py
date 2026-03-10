import xml.etree.ElementTree as ET

class Empleados:
    def __init__(self, nombre, ID, salario, años_experiencia):
        self.nombre = nombre
        self.ID = ID
        self.salario = salario
        self.años_experiencia = años_experiencia
    def calcular_salario(self):
        if self.años_experiencia >= 0 and self.años_experiencia <=2:
            return (self.salario * 0.05) + self.salario
        elif self.años_experiencia >= 3 and self.años_experiencia <=5:
            return (self.salario * 0.10) + self.salario
        elif self.años_experiencia > 5:
            return (self.salario * 0.15) + self.salario
        
    def __str__(self):
        return f"Nombre: {self.nombre}, ID: {self.ID}, Salario: {self.salario}, Años de experiencia: {self.años_experiencia}"  
    
    class GestorEmpleados:
        def __init__(self):
            self.empleados = []
        def agregar_empleado(self, empleado):
            self.empleados.append(empleado)
        def eliminar_empleado(self, ID):
            for empleado in self.empleados:
                if empleado.ID == ID:
                    self.empleados.remove(empleado)
                    return True
            return False
    
        def buscar_empleado(self, ID):
            for empleado in self.empleados:
                if empleado.ID == ID:
                    return empleado
            return None
        
        def editar_empleado(self, ID, nombre=None, salario=None, años_experiencia=None):
            empleado = self.buscar_empleado(ID)
            if empleado:
                if nombre:
                    empleado.nombre = nombre
                if salario:
                    empleado.salario = salario
                if años_experiencia:
                    empleado.años_experiencia = años_experiencia
                return True
            return False
        
        def mostrar_empleados(self):
            for empleado in self.empleados:
                print(empleado)

        def guardar_empleados(self):
            with open("empleados.txt", "w") as file:
                for empleado in self.empleados:
                    file.write(f"{empleado.nombre},{empleado.ID},{empleado.salario},{empleado.años_experiencia}\n")
        
        def cargar_empleados(self):
            try:
                with open("empleados.txt", "r") as file:
                    for line in file:
                        nombre, ID, salario, años_experiencia = line.strip().split(",")
                        empleado = Empleados(nombre, ID, float(salario), int(años_experiencia))
                        self.agregar_empleado(empleado)
            except FileNotFoundError:
                print("No se encontró el archivo.")

class Producto:

    def __init__ (self, nombre: str, id: int, precio: float, cantidadEnInventario: int):
        self.nombre = nombre
        self.id = id
        self.precio = precio
        self.cantidadEnInventario = cantidadEnInventario

    def disminuir_inventario(self, cantidadEnInventario):
        if self.cantidadEnInventario >= cantidadEnInventario:
            self.cantidadEnInventario -= cantidadEnInventario
            return True
        else:
            return False

    def aumentar_inventario(self, cantidadEnInventario):
        self.cantidadEnInventario += cantidadEnInventario

    def mostrar_informacion(self):
        print(f"Producto: {self.nombre} | ID: {self.id} | Precio: {self.precio} | Stock: {self.cantidadEnInventario}")

class Cliente:

    def __init__(self, nombre: str, id: int, saldo: float):
        self.nombre = nombre
        self.id = id
        self.saldo = saldo

    def realizar_compra(self, producto: Producto, cantidad: int):
        if producto.cantidadEnInventario >= cantidad:
            if self.saldo >= producto.precio * cantidad:
                self.saldo -= producto.precio * cantidad
                producto.disminuir_inventario(cantidad)
                return True
            else:
                return False
        else:
            return False

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"ID: {self.id}")
        print(f"Saldo: {self.saldo}")
    
class Tienda:
    def __init__(self):
        self.productos = []
        self.clientes = []
    
    def agregar_producto(self, producto: Producto):
        self.productos.append(producto) 

    def agregar_cliente(self, cliente: Cliente):
        self.clientes.append(cliente)

    def realizar_venta(self, id_cliente: int, id_producto: int, cantidad: int): 
        for cliente in self.clientes:
            if cliente.id == id_cliente:
                for producto in self.productos:
                    if producto.id == id_producto:
                        if cliente.realizar_compra(producto, cantidad):
                            return True
                        else:
                            return False
                return False
        return False    

    def mostrar_productos(self):
        for producto in self.productos:
            producto.mostrar_informacion()

    def mostrar_clientes(self):
        for cliente in self.clientes:
            cliente.mostrar_informacion()

    def guardar_datos(self, archivo: str):
        root = ET.Element("tienda")
        
        productos_elem = ET.SubElement(root, "productos")
        for p in self.productos:
            p_elem = ET.SubElement(productos_elem, "producto")
            ET.SubElement(p_elem, "nombre").text = p.nombre
            ET.SubElement(p_elem, "id").text = str(p.id)
            ET.SubElement(p_elem, "precio").text = str(p.precio)
            ET.SubElement(p_elem, "cantidadEnInventario").text = str(p.cantidadEnInventario)
            
        clientes_elem = ET.SubElement(root, "clientes")
        for c in self.clientes:
            c_elem = ET.SubElement(clientes_elem, "cliente")
            ET.SubElement(c_elem, "nombre").text = c.nombre
            ET.SubElement(c_elem, "id").text = str(c.id)
            ET.SubElement(c_elem, "saldo").text = str(c.saldo)
            
        tree = ET.ElementTree(root)
        try:
            tree.write(archivo, encoding="utf-8", xml_declaration=True)
            print(f"Datos guardados exitosamente en {archivo}")
        except Exception as e:
            print(f"Error al guardar los datos: {e}")

    def cargar_datos(self, archivo: str):
        try:
            tree = ET.parse(archivo)
            root = tree.getroot()
            
            self.productos = []
            productos_elem = root.find("productos")
            if productos_elem is not None:
                for p_elem in productos_elem.findall("producto"):
                    nombre = p_elem.find("nombre").text
                    id_val = int(p_elem.find("id").text)
                    precio = float(p_elem.find("precio").text)
                    cantidad = int(p_elem.find("cantidadEnInventario").text)
                    self.productos.append(Producto(nombre, id_val, precio, cantidad))
                    
            self.clientes = []
            clientes_elem = root.find("clientes")
            if clientes_elem is not None:
                for c_elem in clientes_elem.findall("cliente"):
                    nombre = c_elem.find("nombre").text
                    id_val = int(c_elem.find("id").text)
                    saldo = float(c_elem.find("saldo").text)
                    self.clientes.append(Cliente(nombre, id_val, saldo))
            print(f"Datos cargados exitosamente desde {archivo}")
        except FileNotFoundError:
            print(f"El archivo {archivo} no existe. No se cargaron datos.")
        except ET.ParseError:
            print(f"El archivo {archivo} no tiene un formato XML válido.")
        except Exception as e:
            print(f"Ocurrió un error al cargar los datos: {e}")

class Cesar:
    def __init__(self, k = 0):
        self.k = k
        self.alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        self.alphabetDisplaced = self.alphabet[-self.k:] + self.alphabet[:-self.k]

    def __str__(self):
        return f"{self.alphabet}\n k = {self.k}\n{self.alphabetDisplaced}"
    
    def modifyK(self, k):
        self.k = k
        self.alphabetDisplaced = self.alphabet[-self.k:] + self.alphabet[:-self.k]

    def encode(self, text):
        encryptedText = ""
        for i in range(len(text)):
            if text[i] != ' ':
                encryptedText += self.alphabetDisplaced[self.alphabet.index(text[i])]
            else:
                encryptedText += ' '

        return encryptedText
    
    def deEncode(self, encryptedText):
        text = ""
        for i in range(len(encryptedText)):
            if encryptedText[i] != ' ':
                text += self.alphabet[self.alphabetDisplaced.index(encryptedText[i])]
            else:
                text += ' '

        return text


def menu_empleados():
    gestor = Empleados.GestorEmpleados()
    gestor.cargar_empleados()

    while True:
        print("\nSistema de Gestión de Empleados")
        print("1. Agregar empleado")
        print("2. Eliminar empleado")
        print("3. Buscar empleado por ID")
        print("4. Mostrar empleados")
        print("5. Guardar empleados")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            ID = input("ID: ")
            salario = float(input("Salario: "))
            años = int(input("Años de experiencia: "))

            empleado = Empleados(nombre, ID, salario, años)
            gestor.agregar_empleado(empleado)
            print("Empleado agregado correctamente.")

        elif opcion == "2":
            ID = input("Ingrese el ID del empleado a eliminar: ")
            if gestor.eliminar_empleado(ID):
                print("Empleado eliminado.")
            else:
                print("Empleado no encontrado.")

        elif opcion == "3":
            ID = input("Ingrese el ID a buscar: ")
            empleado = gestor.buscar_empleado(ID)

            if empleado:
                print("\nEmpleado encontrado:")
                print(empleado)
                print("Salario con aumento:", empleado.calcular_salario())
            else:
                print("Empleado no encontrado.")

        elif opcion == "4":
            print("\nLista de empleados:")
            gestor.mostrar_empleados()

        elif opcion == "5":
            gestor.guardar_empleados()
            print("Empleados guardados en archivo.")

        elif opcion == "6":
            gestor.guardar_empleados()
            print("Saliendo del sistema...")
            main()
            break

        else:
            print("Opción inválida.")

def menu_tienda():
    mi_tienda = Tienda()

    while True:
        print("\nSistema de Gestión de Tienda")
        print("1. Agregar producto")
        print("2. Agregar cliente")
        print("3. Realizar venta")
        print("4. Mostrar productos")
        print("5. Mostrar clientes")
        print("6. Guardar datos en XML")
        print("7. Cargar datos desde XML")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            id_producto = int(input("ID del producto: "))
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad en inventario: "))

            producto = Producto(nombre, id_producto, precio, cantidad)
            mi_tienda.agregar_producto(producto)
            print("Producto agregado correctamente.")

        elif opcion == "2":
            nombre = input("Nombre del cliente: ")
            id_cliente = int(input("ID del cliente: "))
            saldo = float(input("Saldo del cliente: "))

            cliente = Cliente(nombre, id_cliente, saldo)
            mi_tienda.agregar_cliente(cliente)
            print("Cliente agregado correctamente.")

        elif opcion == "3":
            id_cliente = int(input("ID del cliente: "))
            id_producto = int(input("ID del producto: "))
            cantidad = int(input("Cantidad a comprar: "))
            if mi_tienda.realizar_venta(id_cliente, id_producto, cantidad):
                print("Venta realizada con éxito.")
            else:
                print("No se pudo realizar la venta.")

        elif opcion == "4":
            print("\n--- LISTA DE PRODUCTOS ---")
            mi_tienda.mostrar_productos()

        elif opcion == "5":
            print("\n--- LISTA DE CLIENTES ---")
            mi_tienda.mostrar_clientes()

        elif opcion == "6":
            mi_tienda.guardar_datos("tienda.xml")

        elif opcion == "7":
            mi_tienda.cargar_datos("tienda.xml")

        elif opcion == "8":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")

def ejercicio4():
    print("Punto 4 del parcial I\n")
    num = (int(input("Ingrese un numero de 4 cifras: ")))

    firstDigit = num // 1000
    secondDigit = (num % 1000) // 100
    thirdDigit = (num % 100) // 10
    fourthDigit = num % 10

    if firstDigit % fourthDigit == 0:
        print(f"{firstDigit} SI es multiplo de {fourthDigit}")
    else:
        print(f"{firstDigit} NO es multiplo de {fourthDigit}")

    sumSecondThird = secondDigit + thirdDigit
    print (f"La suma del secondDigit y el tercer numero es: {sumSecondThird}")

def julio_cesar():
    print("Este es un codigo que con una clase 'Cesar' que recibe un desplazamiento 'k' y usando sus metodos se puede cifrar o decifrar una palabra con la 'k' dada.")
    
    encription = Cesar(0)
    while 1:
        # print(encription)

        print("\n--- MENÚ ---")
        print("1. Ingresar desplazamiento")
        print("2. Encriptar una frase")
        print("3. Desencriptar una frase")
        print("4. Salir")

        opcion = int(input("\nSeleccione una opción: "))

        if opcion == 1:
            encription.modifyK(int(input("\nIngrese el desplazamiento para el cifrado: ")))
            print(encription)
        elif opcion == 2:
            phrase = input("\nIngrese la frase a encriptar: ").lower()
            encryptedPhrase = encription.encode(phrase)
            print(f"\nFrase = {phrase}\nEncriptado = {encryptedPhrase}")
        elif opcion == 3:
            encryptedPhrase = input("\nIngrese la frase a desencriptar: ").lower()
            phrase = encription.deEncode(encryptedPhrase)
            print(f"\nEncriptado = {encryptedPhrase}\nFrase = {phrase}")
        elif opcion == 4:
            print("\nSaliendo...")
            break
        else:
            print("Opción no valida, intente de nuevo.")

def main():
    opc = int(input("\nIngrese el numero del ejercicio a ejecutar (2, 3, 4 o 5) o 1 para salir: "))
    
    while opc != 1:
        if opc == 2:
            menu_empleados()
        elif opc == 3:
            menu_tienda()
        elif opc == 4:
            ejercicio4()
        elif opc == 5:
            julio_cesar()
        else:
            print("Opción no valida.")

        opc = int(input("\nIngrese el numero del ejercicio a ejecutar (2, 3, 4 o 5) o 1 para salir: "))

main()
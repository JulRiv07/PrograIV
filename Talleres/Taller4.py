def ejercicio1():
    class Persona:
        def __init__(self, nombre, edad):
            self.nombre = nombre
            self.edad = edad

        def __str__(self):
            return f"Nombre: {self.nombre}, Edad: {self.edad}"
        
    persona1 = Persona("Juan", 30)
    persona2 = Persona("María", 25)
    persona3 = Persona("Carlos", 40)

    print(persona1) 
    print(persona2)
    print(persona3)

def ejercicio2():
    class Libro:
        def __init__(self, titulo, autor):
            self.titulo = titulo
            self.autor = autor

        def __str__(self):
            return f"'{self.titulo}' por {self.autor}"
        
    libro1 = Libro("El principito", "Antoine de Saint-Exupéry")
    libro2 = Libro("Cien años de soledad", "Gabriel García Márquez")
    libro3 = Libro("1984", "George Orwell")
    libro4 = Libro("Don Quijote", "Miguel de Cervantes")
    libro5 = Libro("La Odisea", "Homero")  
    libros = [libro1, libro2, libro3, libro4, libro5]
    
    print("Libros en la biblioteca: ")
    for libro in libros:
        print(libro)

def ejercicio3():
    class Playlist:
        def __init__(self, nombre_playlist):
            self.nombre_playlist = nombre_playlist
            self.canciones = []

        def agregar_cancion(self, cancion):
            self.canciones.append(cancion)
        
        def __len__(self):
            return len(self.canciones)
        
    playlist_de_Julian = Playlist("Playlist de Julian")
    playlist_de_Julian.agregar_cancion("Shape of You")
    playlist_de_Julian.agregar_cancion("Blinding Lights")
    playlist_de_Julian.agregar_cancion("Levitating")
    playlist_de_Julian.agregar_cancion("Despacito")
    playlist_de_Julian.agregar_cancion("Believer")
    playlist_de_Julian.agregar_cancion("Perfect")
    
    print("\nPlaylist:", playlist_de_Julian.nombre_playlist)
    print(f"La cantidad de canciones en la playlist es: {len(playlist_de_Julian)}")

def ejercicio4():
    class EquipoFutbol:
        def __init__(self, nombre_equipo):
            self.nombre_equipo = nombre_equipo
            self.jugadores = []
        
        def agregar_jugador(self, jugador):
            self.jugadores.append(jugador)
        
        def __len__(self):
            return len(self.jugadores)
        
    equipo1 = EquipoFutbol("Tigres")
    equipo2 = EquipoFutbol("Leones")

    equipo1.agregar_jugador("Carlitos")
    equipo1.agregar_jugador("Luis")
    equipo1.agregar_jugador("Juanma")

    equipo2.agregar_jugador("David")
    equipo2.agregar_jugador("Mario")

    print("\nEquipo: ", equipo1.nombre_equipo)
    print(f"Cantidad de jugadores en el equipo: {len(equipo1)}")

    print("\nEquipo: ", equipo2.nombre_equipo)
    print(f"Cantidad de jugadores en el equipo: {len(equipo2)}")    

def ejercicio5():
    class Producto:
        def __init__(self, nombre, precio):
            self.nombre = nombre
            self.precio = precio
        
        def __add__(self, otro_producto):
            return self.precio + otro_producto.precio
        
    producto1 = Producto("Mac", 1000)
    producto2 = Producto("Iphone", 500)

    print("\n Producto 1: ", producto1.nombre, "Precio: $", producto1.precio)
    print("Producto 2: ", producto2.nombre, "Precio: $", producto2.precio)
    print(f"El precio total de ambos productos es: ${producto1 + producto2}")

def ejercicio6():
    class Vector2D:
        
        def __init__(self, x, y):
            self.x = x
            self.y = y
        
        def __add__(self, otro):
            nuevo_x = self.x + otro.x
            nuevo_y = self.y + otro.y
            return Vector2D(nuevo_x, nuevo_y)
        
        def __str__(self):
            return f"Vector2D({self.x}, {self.y})"
        
    v1 = Vector2D(2, 3)
    v2 = Vector2D(4, 5)
    resultado = v1 + v2

    print("\nVector 1: ", v1)
    print("Vector 2: ", v2)
    print("Resultado de la suma de los vectores: ", resultado)
    
def ejercicio7():
    class Estudiante:
        def __init__(self, nombre, codigo):
            self.nombre = nombre
            self.codigo = codigo

        def __eq__(self, otro):
            return self.codigo == otro.codigo
        
    est1 = Estudiante("Carlos", 101)
    est2 = Estudiante("Ana", 102)
    est3 = Estudiante("Luis", 101)

    print("\nComparaciones: ")
    print("est1 == est2: ", est1 == est2)
    print("est1 == est3: ", est1 == est3)

def ejercicio8():
    class CarritoCompras:
        def __init__(self):
            self.productos = []

        def agregar_producto(self, producto):
            self.productos.append(producto)

        def __len__(self):
            return len(self.productos)
        
        def __str__(self):
            lista = "Productos en el carrito:\n"
            for producto in self.productos:
                lista += f"- {producto}\n"
            return lista
        
    carrito = CarritoCompras()
    carrito.agregar_producto("Manzana")
    carrito.agregar_producto("Pan")
    carrito.agregar_producto("Leche")
    carrito.agregar_producto("Huevos")
    print(carrito)
    print(f"Cantidad de productos en el carrito: {len(carrito)}")

def ejercicio9():
    class Biblioteca:
        def __init__(self):
            self.libros = []

        def agregar_libro(self, libro):
            self.libros.append(libro)

        def __len__(self):
            return len(self.libros)
        
        def __add__(self, otros):
            nueva_biblioteca = Biblioteca()
            nueva_biblioteca.libros = self.libros + otros.libros
            return nueva_biblioteca
        
    b1 = Biblioteca()
    b2 = Biblioteca()

    b1.agregar_libro("El principito")
    b1.agregar_libro("1984")

    b2.agregar_libro("Don Quijote")
    b2.agregar_libro("La Odisea")
    biblioteca_total = b1 + b2

    print("\nLibros en biblioteca total: ", len(biblioteca_total))
    for libro in biblioteca_total.libros:
        print("-" + libro)

def ejercicio10():

    class Estudiante:
        def __init__(self, nombre, codigo):
            self.nombre = nombre
            self.codigo = codigo

        def __eq__(self, otro):
            return self.codigo == otro.codigo
        
        def __str__(self):
            return f"{self.nombre} ({self.codigo})"

    class Curso:

        def __init__(self, nombre_curso):
            self.nombre_curso = nombre_curso
            self.estudiantes = []

        def agregar_estudiante(self, estudiante):
            self.estudiantes.append(estudiante)

        def __len__(self):
            return len(self.estudiantes)
        
        def __str__(self):
            texto = f"Curso: {self.nombre_curso}\nEstudiantes:\n"
            for estudiante in self.estudiantes:
                texto += f"- {estudiante}\n"

            return texto

        def __eq__(self, otros):
            return len(self.estudiantes) == len(otros.estudiantes)
        
    e1 = Estudiante("Carlos", 101)
    e2 = Estudiante("Ana", 102)
    e3 = Estudiante("Luis", 103)

    curso1 = Curso("Programación")
    curso2 = Curso("Bases de Datos")

    curso1.agregar_estudiante(e1)
    curso1.agregar_estudiante(e2)

    curso2.agregar_estudiante(e3)
    curso2.agregar_estudiante(e2)

    print(len(curso1))
    print(curso1)
    print(curso1 == curso2)   

def menu():
    while True:
        print("\n TALLER IV - Menu")
        print("1. Ejercicio 1")
        print("2. Ejercicio 2")
        print("3. Ejercicio 3")
        print("4. Ejercicio 4")
        print("5. Ejercicio 5")
        print("6. Ejercicio 6")
        print("7. Ejercicio 7")
        print("8. Ejercicio 8")
        print("9. Ejercicio 9 ")
        print("10. Ejercicio 10")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ejercicio1()
        elif opcion == "2":
            ejercicio2()
        elif opcion == "3":
            ejercicio3()
        elif opcion == "4":
            ejercicio4()
        elif opcion == "5":
            ejercicio5()
        elif opcion == "6":
            ejercicio6()
        elif opcion == "7":
            ejercicio7()
        elif opcion == "8":
            ejercicio8()
        elif opcion == "9":
            ejercicio9()
        elif opcion == "10":
            ejercicio10()
        elif opcion == "0":
            print("Ha sido un placer...")
            break
        else:
            print("Incorrectaaaa!!!")

menu()
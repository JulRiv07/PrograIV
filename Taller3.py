import datetime

class Libro:

    def __init__(self, titulo, autor, año, editorial, genero):
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.editorial = editorial
        self.genero = genero
        
    def mostrar_info(self):
        print("Titulo:", self.titulo)
        print("Autor:", self.autor)
        print("Año:", self.año)
        print("Editorial:", self.editorial)
        print("Genero:", self.genero)
    
    def guardar_archivo(self):
        archivo = open("libros.txt", "a")
        archivo.write(self.titulo + "," + self.autor + "," + str(self.año) + "," + self.editorial + "," + self.genero + "\n")
        archivo.close()

class Estudiante:
    def __init__ (self, nombre, codigo, carrera, edad, promedio):
        self.nombre = nombre
        self.codigo = codigo
        self.carrera = carrera
        self.edad = edad
        self.promedio = promedio

        def mostrar_info(self):
            print("Nombre:", self.nombre)
            print("Código:", self.codigo)
            print("Carrera:", self.carrera)
            print("Edad:", self.edad)
            print("Promedio:", self.promedio)

        def guardar_archivo(self):
            archivo = open("estudiantes.txt", "a")
            archivo.write(self.nombre + "," + self.codigo + "," + self.carrera + "," + str(self.edad) + "," + str(self.promedio) + "\n")
            archivo.close() 

class InventarioProducto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def añadir_producto(self):
        archivo = open("inventario.txt", "a")
        archivo.write(self.nombre + "," + str(self.cantidad) + "," + str(self.precio) + "\n")
        archivo.close()

class Vehiculo:
    def __init__(self, marca, modelo, año, tipo, placa):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.tipo = tipo
        self.placa = placa

    def mostrar_info(self):

        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Año:", self.año)
        print("Tipo:", self.tipo)
        print("Placa:", self.placa)
    
    def guardar_si_actual(self):

        año_actual = datetime.datetime.now().year

        if self.año == año_actual:
            archivo = open("vehiculos_actuales.txt", "a")
            archivo.write(self.marca + "," + self.modelo + "," + str(self.año) + "," + self.tipo + "," + self.placa + "\n")
            archivo.close()
            print("Vehículo guardado (año actual).")

        else:
            print("El vehículo no es del año actual, no se guardó.")

class Encuesta:
    def __init__(self, edad, genero, ciudad, opinion):
        self.edad = edad
        self.genero = genero
        self.ciudad = ciudad
        self.opinion = opinion

    def guardar_respuesta(self):

        nombre_archivo = "encuesta_" + self.ciudad.lower() + ".txt"

        archivo = open(nombre_archivo, "a")
        archivo.write(str(self.edad) + "," + self.genero + "," + self.ciudad + "," + self.opinion + "\n")
        archivo.close()

        print("Respuesta guardada en", nombre_archivo)

class NotaMusical:
    def __init__(self, nota, frecuencia, duracion):
        self.nota = nota
        self.frecuencia = frecuencia
        self.duracion = duracion

    def ejecutar(self):

        print("Reproduciendo nota:", self.nombre)
        print("Frecuencia:", self.frecuencia, "Hz")
        print("Duración:", self.duracion, "segundos")

    def guardar_si_mayor(self, frecuencia_min):

        if self.frecuencia > frecuencia_min:
            archivo = open("notas_altas.txt", "a")
            archivo.write(self.nombre + "," + str(self.frecuencia) + "," + str(self.duracion) + "\n")
            archivo.close()
            print("Nota guardada.")
        else:
            print("La nota no supera la frecuencia mínima.")
    
class AgendaContactos:
    def __init__(self, nombre, telefono, correo, direccion):
        self.nombre = nombre
        self.telefono = telefono
        self.email = correo
        self.direccion = direccion

    def buscar_contacto(self, nombre_buscar):
        archivo = open("agenda.txt", "r")
        for linea in archivo:
            datos = linea.strip().split(",")
            if datos[0].lower() == nombre_buscar.lower():
                print("Nombre:", datos[0])
                print("Teléfono:", datos[1])
                print("Correo:", datos[2])
                print("Dirección:", datos[3])
                print()
        archivo.close()

    def eliminar_contacto(self, nombre_eliminar):
        archivo = open("agenda.txt", "r")
        lineas = archivo.readlines()
        archivo.close()

        with open("agenda.txt", "w") as archivo:
            for linea in lineas:
                datos = linea.strip().split(",")
                if datos[0].lower() != nombre_eliminar.lower():
                    archivo.write(linea)

        archivo.close()
        print("Contacto eliminado si existía.")

    def actualizar_contacto(self, nombre_actualizar, nuevo_telefono, nuevo_email, nueva_direccion):
        archivo = open("agenda.txt", "r")
        lineas = archivo.readlines()
        archivo.close()

        with open("agenda.txt", "w") as archivo:
            for linea in lineas:
                datos = linea.strip().split(",")
                if datos[0].lower() == nombre_actualizar.lower():
                    archivo.write(nombre_actualizar + "," + nuevo_telefono + "," + nuevo_email + "," + nueva_direccion + "\n")
                else:
                    archivo.write(linea)

        archivo.close()

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3
    
    def calcular_area(self): 
        s = self.calcular_perimetro() / 2
        area = (s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3)) ** 0.5
        return area
    
    def triangulo(self):
        if self.lado1 == self.lado2 == self.lado3:
            return "Equilátero"
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            return "Isósceles"
        else: 
            return "Escaleno"
        
class Empresa:
    def __init__(self, empleado, salario, bonificaciones, descuentos):
        self.empleado = empleado
        self.salario = salario
        self.bonificaciones = bonificaciones
        self.descuentos = descuentos

    def salario_final(self):
        return self.salario + self.bonificaciones - self.descuentos
    
    def guardar_reporte(self):
        nombre_archivo = "Empleado_" + self.departamento.lower() + ".txt"
        archivo = open(nombre_archivo, "a")
        salario_final = self.calcular_salario_final()
        archivo.write(self.nombre + "," + self.departamento + "," + str(self.salario) + "," + str(self.bonificaciones) + "," + str(self.descuentos) + "," + str(salario_final) + "\n" )
        archivo.close()
    
class SistemaNotas:
    def __init__(self):
        self.estudiantes = []

    def agregar_estudiante(self, nombre, materia, nota):
        estudiante = {"nombre": nombre, "materia": materia, "nota": nota}
        self.estudiantes.append(estudiante)
    
    def promedio_materia(self, materia):
        suma = 0
        cantidad = 0
        for e in self.estudiantes:
            if e["materia"].lower() == materia.lower():
                promedio = sum(e["notas"]) / len(e["notas"])
                suma += promedio
                cantidad += 1

            if cantidad > 0:
                print("El promedio de la materia", materia, "es:", suma / cantidad)
            else:
                print("No se encontraron estudiantes para la materia", materia)

    def mejores(self):
        archivo = open("mejores_estudiantes.txt", "w")
        for e in self.estudiantes:
            promedio = sum(e["notas"]) / len(e["notas"])
            if promedio >= 4.0:
                archivo.write(e["nombre"] + "," + e["materia"] + "," + str(promedio) + "\n")
        archivo.close()
        print("Mejores estudiantes guardados en mejores_estudiantes.txt")

def valor_total():
    archivo = open("inventario.txt", "r")
    total = 0
    for linea in archivo:
        datos = linea.strip().split(",")
        cantidad = int(datos[1])
        precio = float(datos[2])

    archivo.close()
    print("El valor total del inventario es:", total)

def buscar_por_autor(autor_buscar):

    archivo = open("libros.txt", "r")

    for linea in archivo:
        datos = linea.strip().split(",")

        if datos[1].lower() == autor_buscar.lower():
            print("Título:", datos[0])
            print("Autor:", datos[1])
            print("Año:", datos[2])
            print("Editorial:", datos[3])
            print("Género:", datos[4])
            print()

    archivo.close()

def calcular_promedio(self, notas):
    suma = 0
    notas = int(input("Ingrese el numero de notas que desea ingresar: "))
    for i in range(notas):
        nota = float(input(f"Ingrese la nota {i+1}: "))
        suma += nota
            
    self.promedio = suma / notas
    print("El promedio del estudiante es:", self.promedio)

def leer_vehiculos():

    archivo = open("vehiculos_actuales.txt", "r")

    for linea in archivo:

        datos = linea.strip().split(",")

        print("Marca:", datos[0])
        print("Modelo:", datos[1])
        print("Año:", datos[2])
        print("Tipo:", datos[3])
        print("Placa:", datos[4])
        print()

    archivo.close()

def estadisticas_genero(ciudad):

    nombre_archivo = "encuesta_" + ciudad.lower() + ".txt"

    archivo = open(nombre_archivo, "r")

    masculino = 0
    femenino = 0
    otros = 0

    for linea in archivo:

        datos = linea.strip().split(",")

        genero = datos[1].lower()

        if genero == "masculino":
            masculino += 1

        elif genero == "femenino":
            femenino += 1

        else:
            otros += 1

    archivo.close()

    print("Estadísticas de género en", ciudad)
    print("Masculino:", masculino)
    print("Femenino:", femenino)
    print("Otros:", otros)

def leer_notas():

    archivo = open("notas_altas.txt", "r")

    for linea in archivo:

        datos = linea.strip().split(",")

        print("Nombre:", datos[0])
        print("Frecuencia:", datos[1])
        print("Duración:", datos[2])
        print()

    archivo.close()

def leer_reporte(departamento):

    nombre_archivo = "empleados_" + departamento.lower() + ".txt"

    archivo = open(nombre_archivo, "r")

    for linea in archivo:

        datos = linea.strip().split(",")

        print("Nombre:", datos[0])
        print("Departamento:", datos[1])
        print("Salario:", datos[2])
        print("Bonificación:", datos[3])
        print("Descuento:", datos[4])
        print("Salario final:", datos[5])
        print()

    archivo.close()

def libros():

    while True:

        print("\n1. Agregar libro")
        print("2. Buscar libro por autor")
        print("3. Volver al menu principal")

        opc = int(input("Seleccione una opcion: "))

        if opc == 1:

            titulo = input("Titulo: ")
            autor = input("Autor: ")
            año = input("Año: ")
            editorial = input("Editorial: ")
            genero = input("Genero: ")

            libro = Libro(titulo, autor, año, editorial, genero)

            libro.mostrar_info()
            libro.guardar_archivo()

        elif opc == 2:

            autor = input("Ingrese el autor a buscar: ")
            buscar_por_autor(autor)

        elif opc == 3:
            break

def estudiantes():
    while True:

        print("\n1. Agregar estudiante")
        print("2. Calcular promedio")
        print("3. Volver al menu principal")

        opc = int(input("Seleccione una opcion: "))

        if opc == 1:

            nombre = input("Nombre: ")
            codigo = input("Código: ")
            carrera = input("Carrera: ")
            edad = input("Edad: ")

            estudiante = Estudiante(nombre, codigo, carrera, edad, 0)

            estudiante.mostrar_info()
            estudiante.guardar_archivo()

        elif opc == 2:
            estudiante.calcular_promedio()

        elif opc == 3:
            break

def inventario():
    while True:

        print("\n1. Agregar producto")
        print("2. Calcular valor total del inventario")
        print("3. Volver al menu principal")

        opc = int(input("Seleccione una opcion: "))

        if opc == 1:

            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))

            producto = InventarioProducto(nombre, cantidad, precio)

            producto.añadir_producto()

        elif opc == 2:
            valor_total()

        elif opc == 3:
            break

def vehiculos():
    while True:

        print("\n1. Registrar vehículo")
        print("2. Ver vehículos del año actual")
        print("3. Volver al menú")

        opc = int(input("Seleccione una opción: "))

        if opc == 1:

            marca = input("Marca: ")
            modelo = input("Modelo: ")
            año = int(input("Año: "))
            tipo = input("Tipo: ")
            placa = input("Placa: ")

            vehiculo = Vehiculo(marca, modelo, año, tipo, placa)

            vehiculo.mostrar_info()
            vehiculo.guardar_si_actual()

        elif opc == 2:
            leer_vehiculos()

        elif opc == 3:
            break

def encuestas():

    while True:

        print("\n1. Registrar respuesta")
        print("2. Ver estadísticas por género")
        print("3. Volver al menú")

        opc = int(input("Seleccione una opción: "))

        if opc == 1:

            edad = int(input("Edad: "))
            genero = input("Genero: ")
            ciudad = input("Ciudad: ")
            opinion = input("Opinión: ")

            encuesta = Encuesta(edad, genero, ciudad, opinion)

            encuesta.guardar_respuesta()

        elif opc == 2:

            ciudad = input("Ingrese la ciudad: ")
            estadisticas_genero(ciudad)

        elif opc == 3:
            break

def notas_musicales():

    while True:

        print("\n1. Registrar nota musical")
        print("2. Ver notas guardadas")
        print("3. Volver al menú")

        opc = int(input("Seleccione una opción: "))

        if opc == 1:

            nombre = input("Nombre de la nota: ")
            frecuencia = float(input("Frecuencia (Hz): "))
            duracion = float(input("Duración (segundos): "))
            nota = NotaMusical(nombre, frecuencia, duracion)
            nota.ejecutar()
            frecuencia_min = float(input("Frecuencia mínima para guardar: "))
            nota.guardar_si_mayor(frecuencia_min)

        elif opc == 2:

            leer_notas()

        elif opc == 3:
            break

def agenda():
    while True:

        print("\n1. Buscar contacto")
        print("2. Eliminar contacto")
        print("3. Actualizar contacto")
        print("4. Volver al menú")

        opc = int(input("Seleccione una opción: "))

        if opc == 1:

            nombre_buscar = input("Ingrese el nombre del contacto a buscar: ")
            contacto = AgendaContactos("", "", "", "")
            contacto.buscar_contacto(nombre_buscar)

        elif opc == 2:

            nombre_eliminar = input("Ingrese el nombre del contacto a eliminar: ")
            contacto = AgendaContactos("", "", "", "")
            contacto.eliminar_contacto(nombre_eliminar)

        elif opc == 3:

            nombre_actualizar = input("Ingrese el nombre del contacto a actualizar: ")
            nuevo_telefono = input("Nuevo teléfono: ")
            nuevo_email = input("Nuevo correo: ")
            nueva_direccion = input("Nueva dirección: ")

            contacto = AgendaContactos("", "", "", "")
            contacto.actualizar_contacto(nombre_actualizar, nuevo_telefono, nuevo_email, nueva_direccion)

        elif opc == 4:
            break

def triangulo():
    while True:
        print("\n1. Calcular área y perímetro")
        print("2. Determinar tipo de triángulo")
        print("3. Volver al menú")

        opc = int(input("Seleccione una opción: "))

        if opc == 1:

            lado1 = float(input("Lado 1: "))
            lado2 = float(input("Lado 2: "))
            lado3 = float(input("Lado 3: "))

            triangulo = Triangulo(lado1, lado2, lado3)

            area = triangulo.calcular_area()
            perimetro = triangulo.calcular_perimetro()

            print("Área del triángulo:", area)
            print("Perímetro del triángulo:", perimetro)

        elif opc == 2:

            lado1 = float(input("Lado 1: "))
            lado2 = float(input("Lado 2: "))
            lado3 = float(input("Lado 3: "))

            triangulo = Triangulo(lado1, lado2, lado3)

            tipo = triangulo.triangulo()
            print("El triángulo es:", tipo)

        elif opc == 3:
            break

def sistema_notas():
    while True: 
        print("\n1. Agregar estudiante y nota")
        print("2. Calcular promedio de materia")
        print("3. Guardar mejores estudiantes")
        print("4. Volver al menú")

        opc = int(input("Seleccione una opción: "))

        if opc == 1:

            nombre = input("Nombre del estudiante: ")
            materia = input("Materia: ")
            nota = float(input("Nota: "))

            sistema = SistemaNotas()
            sistema.agregar_estudiante(nombre, materia, nota)

        elif opc == 2:

            materia = input("Ingrese la materia: ")
            sistema.promedio_materia(materia)

        elif opc == 3:
            sistema.mejores()

        elif opc == 4:
            break

def empresa():
    while True:
        print("\n1. Calcular salario final")
        print("2. Guardar reporte de empleado")
        print("3. Ver reporte de departamento")
        print("4. Volver al menú")

        opc = int(input("Seleccione una opción: "))

        if opc == 1:

            nombre = input("Nombre del empleado: ")
            departamento = input("Departamento: ")
            salario = float(input("Salario base: "))
            bonificaciones = float(input("Bonificaciones: "))
            descuentos = float(input("Descuentos: "))

            empleado = Empresa(nombre, salario, bonificaciones, descuentos)

            salario_final = empleado.salario_final()
            print("El salario final del empleado es:", salario_final)

        elif opc == 2:

            nombre = input("Nombre del empleado: ")
            departamento = input("Departamento: ")
            salario = float(input("Salario base: "))
            bonificaciones = float(input("Bonificaciones: "))
            descuentos = float(input("Descuentos: "))

            empleado = Empresa(nombre, salario, bonificaciones, descuentos)
            empleado.guardar_reporte()

        elif opc == 3:

            departamento = input("Ingrese el departamento: ")
            leer_reporte(departamento)

        elif opc == 4:
            break

def menu():
    while True:
        print("\nMENÚ PRINCIPAL...\n")
        print("1. Gestión de Libros")
        print("2. Gestión de Estudiantes")
        print("3. Inventario de Productos")
        print("4. Registro de Vehículos")
        print("5. Encuesta de Usuarios")
        print("6. Notas Musicales")
        print("7. Agenda de Contactos")
        print("8. Triángulo (Área y Perímetro)")
        print("9. Sistema de Empresa")
        print("10. Sistema de Notas")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Ejecutando sistema de libros...")
            libros()

        elif opcion == "2":
            print("Ejecutando sistema de estudiantes...")
            estudiantes()

        elif opcion == "3":
            print("Ejecutando inventario...")
            inventario()

        elif opcion == "4":
            print("Ejecutando registro de vehículos...")
            vehiculos()

        elif opcion == "5":
            print("Ejecutando encuesta...")
            encuestas()

        elif opcion == "6":
            print("Ejecutando notas musicales...")
            notas_musicales()

        elif opcion == "7":
            print("Ejecutando agenda de contactos...")
            agenda()

        elif opcion == "8":
            print("Ejecutando cálculo de triángulo...")
            triangulo()

        elif opcion == "9":
            print("Ejecutando sistema de empresa...")
            empresa()

        elif opcion == "10":
            print("Ejecutando sistema de notas...")
            sistema_notas()

        elif opcion == "0":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")


def main():
    menu()

main()

#By Julian Rivera - 2026-1
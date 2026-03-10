from io import *
from datetime import datetime, timedelta

def Num_Y_Dig_Invertidos():

    class Numero:
        def __init__(self, valor):
            if 100 <= valor <= 999:
                self.valor = valor
            else:
                raise ValueError("El número debe tener tres cifras")

        def suma_digitos(self):
            suma = 0
            for digito in str(self.valor):
                suma += int(digito)
            return suma

        def escribir_archivo(self):
            invertido = str(self.valor)[::-1]
            with open("numeros.txt", "a") as archivo:
                archivo.write("Original: " + str(self.valor) + " - Invertido: " + invertido + "\n")

    try:
        num = int(input("Ingrese un número de tres cifras: "))
        n = Numero(num)

        print("Suma de dígitos:", n.suma_digitos())

        n.escribir_archivo()

        print("\nContenido del archivo:")
        with open("numeros.txt", "r") as archivo:
            print(archivo.read())

    except ValueError as e:
        print("Error:", e)

def Conteo_frases():
    class Frase:
        def __init__(self, texto, autor):
            self.texto = texto
            self.autor = autor
        
    frases = []
    cantidad = int(input("¿Cuantas frases desea ingresar? : " ))

    for i in range(cantidad):
        texto = input(f"Frase {i + 1} :")
        autor = input("Autor: ")
        frases.append(Frase(texto, autor))    

    palabra = input("Ingrese la palabra a buscar: ")

    total = 0
    for f in frases:
        texto_minuscula = f.texto.lower()
        palabra_minuscula = palabra.lower()
        total += texto_minuscula.count(palabra_minuscula)

    with open("frases.txt", "w") as f:
        f.write(f"La palabra '{palabra}' aparece un total de: {total} veces ")
    
    print("Ready, todo guardado en frases.txt")

def cadenas_vocales():
    
    class cadena: 
        def __init__(self, texto):
            self.texto = texto
    
    lista = []
    for i in range(15):
        texto = input(f"Ingrese la cadena #{i+1}: ")
        lista.append(cadena(texto))

    vocales = "aeiouAEIOU"
    ordenadas = sorted(lista, key = lambda c: c.texto[0] not in vocales)

    with open("cadenas.txt", "w") as f:
        for cadena in ordenadas:
            f.write(cadena.texto + "\n")

    print("Cadenas ordenadas guardadas!!")

def Registro_clientes():

    class Cliente:
        def __init__(self, id, nombre, edad, ciudad, saldo):
            self.id = id
            self.nombre = nombre
            self.edad = edad
            self.ciudad = ciudad
            self.saldo = saldo

    cantidad = int(input("Ingrese la cantidad de clientes que desea ingresar: "))

    with open("clientes.txt", "w") as f:
        for i in range(cantidad):
            id = input("ID: ")
            nombre = input("Nombre: ")
            edad = input("Edad: ")
            ciudad = input("Ciudad: ")
            saldo = float(input("Saldo: "))
            f.write(f"{id}, {nombre}, {edad}, {ciudad}, {saldo}\n")

    print("\n Clientes con saldo negativo: ")
    with open("clientes.txt", "r") as f:
        for linea in f:
            datos = linea.strip().split(",")
            if float(datos[4]) < 0:
                print(datos[1])        

def Electrodomesticos():
    class Electrodomestico:
        def __init__(self, nombre, marca, consumo):
            self.nombre = nombre
            self.marca = marca
            self.consumo = consumo

        def clasificar(self):
            return "Bajo cosnumo" if self.consumo < 500 else "Alto consumo"
    
    cantidad = int(input("¿Cuantos electrodomesticos desea ingresar?: "))

    with open("electrodomesticos.txt", "w") as f:
        for i in range(cantidad):
            nombre = input("Nombre: ")
            marca = input("Marca: ")
            consumo = float(input("Cosumo en Watts: "))

            e = Electrodomestico(nombre, marca, consumo)
            f.write(f"{nombre}, {marca}, {consumo}, {e.clasificar()} \n")
        
    print("Guardado")

def Animales_Edades():
    class Animal:
        def __init__(self, especie, nombre, edad):
            self.especie = especie
            self.nombre = nombre
            self.edad = edad

    animales = []
    cantidad = int(input("¿Cuántos animales? "))

    for _ in range(cantidad):
        especie = input("Especie: ")
        nombre = input("Nombre: ")
        edad = int(input("Edad: "))
        animales.append(Animal(especie, nombre, edad))

    suma = 0
    for animal in animales:
        suma += animal.edad

    promedio = suma / cantidad

    with open("animales.txt", "w") as f:
        for animal in animales:
            f.write(f"{animal.especie},{animal.nombre},{animal.edad}\n")

    print("Animales que superan el promedio de edad:")
    for animal in animales:
        if animal.edad > promedio:
            print(animal.nombre)

def Inventario_Almacen():
    class Producto:
        def __init__(self, codigo, nombre, cantidad, precio, categoria):
            self.codigo = codigo
            self.nombre = nombre
            self.cantidad = cantidad
            self.precio = precio 
            self.categoria = categoria

    cantidad = int(input("Ingrese la cantidad de productos: "))

    with open("almacen.txt", "w") as f:
        for i in range(cantidad):
            codigo = input("\nCodigo: ")
            nombre = input("Nombre: ")
            cantidad_p = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            categoria = input("Categoría: ")
            f.write(f"{codigo}, {nombre}, {cantidad_p}, {precio}, {categoria} \n")

    totales = {}

    with open("almacen.txt", "r") as f: 
        for linea in f:
            codigo, nombre, cantidad_p, precio, categoria = linea.strip().split(",")
            total = int(cantidad_p) * float(precio)
            totales[categoria] = totales.get(categoria, 0) + total
    
    print("\n Valor total por  categoria: ")
    for elem, total in totales.items():
        print(elem ,":", int(total))


def Agenda_Eventos():
    class Evento:
        def __init__(self, titulo, fecha, hora, lugar, responsable):
            self.titulo = titulo
            self.fecha = fecha
            self.hora = hora
            self.lugar = lugar
            self.responsable = responsable

    cantidad = int(input("Cuantos eventos desea agendar: "))

    with open("agenda.txt", "w") as f:
        for _ in range(cantidad):
            titulo = input("Título: ")
            fecha = input("Fecha (YYYY-MM-DD): ")
            hora = input("Hora: ")
            lugar = input("Lugar: ")
            responsable = input("Responsable: ")
            f.write(f"{titulo},{fecha},{hora},{lugar},{responsable}\n")

    hoy = datetime.now()
    limite = hoy + timedelta(days = 7)

    print("\n Eventos para la proxima semasna: ")
    with open("agenda.txt", "r") as f:
        for linea in f:
            titulo, fecha, hora, lugar, responsable = linea.strip().split(",")
            fecha_evento = datetime.strptime(fecha, "%Y-%m-%d")
            if hoy <= fecha_evento <= limite:
                print(titulo, "-", fecha)

def menu():
    while True:

        print("\n")
        print("*" * 5, "BIENVENIDO", "*" * 5)
        print("1. Números y dígitos invertidos")
        print("2. Conteo de palabras en frases ")
        print("3. Cadenas clasificadas por vocales")
        print("4. Registro de clientes")
        print("5. Clasificación de objetos electrónicos")
        print("6. Animales y edades")
        print("7. Inventario de almacén ")
        print("8. Agenda de eventos")
        print("0. Salir")
        opc = int(input("Ingrese la opcion deseada: "))

        if opc == 0:
            print("bye bye...")
            return
        elif opc == 1: 
            Num_Y_Dig_Invertidos()
        elif opc == 2:
            Conteo_frases()
        elif opc == 3:
            cadenas_vocales()
        elif opc == 4:
            Registro_clientes()
        elif opc == 5:
            Electrodomesticos()
        elif opc == 6:
            Animales_Edades()
        elif opc == 7:
            Inventario_Almacen()
        else:
            Agenda_Eventos()

def main():
    menu()


main()

#By Julian Rivera
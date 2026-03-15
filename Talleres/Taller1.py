import random

def calcular_suma_elementos_numericos():
    total = 0
    lista_datos = [2, 8,"hola", "programación", 10, "utp", 85, 82, 100, "mundo"]
    print("La lista es la siguiente: ", lista_datos)
    for i in range(len(lista_datos)):
        if isinstance(lista_datos[i], int):
            total += lista_datos[i]

    return total

def concatenar_lista_palabras():
    texto_concatenado = ""
    lista_palabras = ["Hola", "mundo", "esto", "es", "python"]
    print("La lista es: ", lista_palabras)
    for i in range(len(lista_palabras)):
        texto_concatenado = texto_concatenado + " " + lista_palabras[i]

    texto_concatenado = texto_concatenado.lstrip()
    return(texto_concatenado)

def promedio_notas_asignaturas():
    asignaturas = []

    numero_de_materias = int(input("¿Cuántas materias desea agregar?: "))

    for i in range(numero_de_materias):
        nombre = input(f"\nIngrese el nombre de la materia {i + 1}: ")
        notas = []

        for j in range(4):
            nota = float(input(f"Ingrese la nota {j + 1} de {nombre}: "))
            notas.append(nota)

        asignaturas.append([nombre, notas])

    suma_promedios = 0

    for materia in asignaturas:
        nombre = materia[0]
        notas = materia[1]

        promedio = sum(notas) / 4
        suma_promedios += promedio

        print(f"\n{nombre} - notas: {notas}")
        print(f"Promedio de {nombre}: {promedio:.2f}")

        if promedio < 3:
            print("Asignatura perdida")
        else:
            print("Asignatura ganada")

    promedio_general = suma_promedios / numero_de_materias
    print(f"\nPromedio general: {promedio_general:.2f}")

    if promedio_general < 3:
        print("Semestre perdido")
    elif 3 <= promedio_general < 4:
        print("Buen trabajo")
    else:
        print("Felicidades serás becado")

def calcular_potencias_lista():
    cantidad_valores = int(input("Ingresa el numero de valores que deseas ingresar: "))
    lista_numeros = [int(input(f"Ingrese el numero {i + 1}: ")) for i in range(cantidad_valores)]

    for i in range(cantidad_valores):
        print(f"{lista_numeros[i]} - {lista_numeros[i] ** 2} - {lista_numeros[i] ** 3}")

def contar_caracteres(cadena):
    total_caracteres = 0
    for i in cadena:
        if i != " ":
            total_caracteres += 1

    return(total_caracteres)

def mayor_y_menor_numero_de_caracteres():
    num = int(input("Ingresa el numero de palabras que deseas ingresar: "))
    lista = [input(f"Ingrese la palabra {i + 1}: ") for i in range(num)]

    mayor = 0
    menor = contar_caracteres(lista[0])
    cadena_mayor = ""
    cadena_menor = lista[0]

    for i in range(num):
        caracteres = contar_caracteres(lista[i])

        if caracteres > mayor:
            mayor = caracteres
            cadena_mayor = lista[i]

        if caracteres < menor:
            menor = caracteres
            cadena_menor = lista[i]

    print(f"Cadena mayor: {cadena_mayor}")
    print(f"Cadena menor: {cadena_menor}")

def buscar_cadena_por_longitud():
    num = int(input("Ingrese un numero: "))
    lista = ["oso", "casa", "murcielago", "ventana", "programacion"]

    for palabra in lista:
        if contar_caracteres(palabra) == num:
            print(f"La palabra con {num} caracteres es: {palabra}")
            return

    print(f"No existe una palabra con {num} caracteres")

def validar_caracter_en_cadenas():
    caracter = input("Ingrese un caracter: ")
    lista = ["oso", "casa", "murcielago", "ventana", "programacion", "objetos", "listas", "metodos", "utp"]
    for i in range(len(lista)):
        for j in lista[i]:
            if j == caracter:
                print(f"La palabra {lista[i]} contiene el caracter {caracter}")
                if contar_caracteres(lista[i]) % 2 == 0:
                    print("La cadena es par")
                else:
                    print("La cadena es impar")

def contar_caracteres_no_vocales():
    lista = ["oso", "casa", "murcielago", "ventana", "programacion", "objetos", "listas", "metodos", "utp", "pereira"]
    total_caracteres = 0
    for i in range(len(lista)):
        for j in lista[i]:
            if j.lower() not in "aeiou" and j != " ":
                total_caracteres += 1
    
    print(f"Caracteres que no son vocales: {total_caracteres}")

def generar_potencias_aleatorias():
    print("\n")
    lista_numeros = [random.randint(1, 100) for i in range(15)]
    for i in range(len(lista_numeros)):
        print(f" {lista_numeros[i]}² = {lista_numeros[i] ** 2}")
        print(f" {lista_numeros[i]}³ = {lista_numeros[i] ** 3} ")
        print("\n")

def varias_operaciones():
    lista = ["casa", "programacion", "utp", "universidad", "utp", "casa", "casa", "thj", "vbh", "456", "987"]
    nueva_lista = []

    for palabra in lista:
        vocal = False
        for letra in palabra:
            if letra.lower() in "aeiou":
                vocal = True

        repetida = False
        for i in nueva_lista:
            if palabra == i:
                repetida = True

        if vocal and not repetida:
            nueva_lista.append(palabra)

    nueva_lista.sort()
    print(nueva_lista)



def main():

    print("-"*50)
    print("Hola, a continuación los ejercicios: ")
    print("1. Sumar los elementos numericos de una lista.")
    print("2. Unir las palabras de una lista")
    print("3. Promedio de materias")
    print("4. Potencia y cubo de numeros en una lista")
    print("5. Cadenas con mayor y menor numero de caracteres")
    print("6. Cadena con mismo numero de caracteres al numero ingresado")
    print("7. Encontrar palabras con el caracter ingresado y decir si son pares o impares")
    print("8. Contar cadenas que no sean vocales")
    print("9. Cuadrado y cubo de aleatorios")
    print("10. Varias operaciones con listas")
    print("0. Salir del menú")
    
    while True:

        opc = int(input("Ingrese la opcion deseada: "))
        print("-"*50)

        if opc == 0:
            print("Saliendo...")
            break
        elif opc == 1:
            print("El resultado de la suma es: ", calcular_suma_elementos_numericos())
        elif opc == 2:
            print("La palabra es: ", concatenar_lista_palabras())
        elif opc == 3:
            promedio_notas_asignaturas()
        elif opc == 4:
            calcular_potencias_lista()
        elif opc == 5:
            mayor_y_menor_numero_de_caracteres()
        elif opc == 6:
            buscar_cadena_por_longitud()
        elif opc == 7:
            validar_caracter_en_cadenas()
        elif opc == 8:
            contar_caracteres_no_vocales()
        elif opc == 9:
            generar_potencias_aleatorias()
        elif opc == 10:
            varias_operaciones()
        else:
            print("Opción incorrecta")
        print("-"*50)

main()

#By Julian Rivera Sanchez
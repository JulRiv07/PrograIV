from .objetos_punto2 import crear_vehiculos
from .clases_punto2 import catalogar

def menu2():
    vehiculos = crear_vehiculos()

    while True:
        print("\nMenú de catálogo de vehículos:")
        print("1. Mostrar todos")
        print("2. Filtrar por 2 ruedas")
        print("3. Filtrar por 4 ruedas")
        print("4. Salir")

        opcion = input("Seleccione: ")

        if opcion == "1":
            catalogar(vehiculos)

        elif opcion == "2":
            catalogar(vehiculos, 2)

        elif opcion == "3":
            catalogar(vehiculos, 4)

        elif opcion == "4":
            print("Bye bye :)")
            break

        else:
            print("Opción inválida")

if __name__ == "__main__":
    menu2()
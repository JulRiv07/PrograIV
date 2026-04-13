from punto1.punto1 import menu1
from punto2.punto2 import menu2
from punto3.punto3 import menu3

def menu_principal():
    print("Seleccione una opción:")
    print("1. Punto 1: Calcular el área de figuras geométricas")
    print("2. Punto 2: Catálogo de vehículos")
    print("3. Punto 3: Menú principal con interfaz gráfica")
    print("4. Salir")

    while True:
        opcion = input("Ingrese el número de la opción deseada: ")
        
        if opcion == '1':
            menu1()
        elif opcion == '2':
            menu2()
            pass
        elif opcion == '3':
            menu3()
            pass
        elif opcion == '4':
            print("Saliendo del programa. Bye bye :)")
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")

if __name__ == "__main__":
    menu_principal()
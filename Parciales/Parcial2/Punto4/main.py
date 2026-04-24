from Parcial2.Punto1.main1 import *
from Parcial2.Punto2.main2 import *
from Parcial2.Punto3.main3 import *

def MostrarMenu():
    print("\n" + "=" * 54)
    print("\t  MENU PARCIAL 2")
    print("=" * 54)
    print("1. Ejecutar Punto 1")
    print("2. Ejecutar Punto 2")
    print("3. Ejecutar Punto 3")
    print("4. Ver vehiculo mas costoso")
    print("5. Ver paciente mas critico")
    print("6. Ver categoria mas vendido")
    print("-" * 54)
    print("  0. Salir")
    print("=" * 54)


def main():
    sistema1 = SistemaAlquiler()
    sistema2 = Sistema()
    sistema3 = Inventario()

    while True:
        MostrarMenu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            main1()

        elif opcion == "2":
            main2()

        elif opcion == "3":
            main3(sistema3)

        elif opcion == "4":
            sistema1.vehiculoCostoso()

        elif opcion == "5":
            menu_reportes()

        elif opcion == "6":
            categoriaMasVendida(sistema3)

        elif opcion == "0":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

main()
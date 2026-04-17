from Parcial2.Punto3.main import *

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

    inv = Inventario()

    while True:
        MostrarMenu()
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            categoriaMasVendida(inv)
        if opcion == "2":
            menu(inv)

        else:
            print("Opción inválida. Intente nuevamente.")

main()
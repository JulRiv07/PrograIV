from services.inventario import Inventario
from models.computador import Computador
from models.celular import Celular
from models.accesorio import Accesorio

inv = Inventario()

while True:
    print("\n--- Menú Principal ---")
    print("1. Registrar")
    print("2. Mostrar")
    print("3. Vender")
    print("4. Reabastecer")
    print("5. Consultar producto")
    print("6. Salir")

    opc = input("Opción: ")
    print()

    if opc == "1":
        codigo = input("Código: ")
        nombre = input("Nombre: ")

        try:
            precio = float(input("Precio: "))
            if precio <= 0:
                print("Precio inválido")
                continue
        except:
            print("Precio inválido")
            continue

        try:
            cantidad = int(input("Cantidad: "))
            if cantidad <= 0:
                print("Cantidad inválida")
                continue
        except:
            print("Cantidad inválida")
            continue

        print()
        tipo = input("Tipo \n1. Computador\n2. Celular\n3. Accesorio\nOpción: ")
        print()

        if tipo == "1":
            ram = input("RAM: ")
            cpu = input("CPU: ")
            p = Computador(codigo, nombre, precio, cantidad, ram, cpu)

        elif tipo == "2":
            alm = input("Almacenamiento: ")
            cam = input("Cámaras: ")
            p = Celular(codigo, nombre, precio, cantidad, alm, cam)

        elif tipo == "3":
            tipoAccesorio = input("Tipo de accesorio: ")
            p = Accesorio(codigo, nombre, precio, cantidad, tipoAccesorio)

        else:
            print("Opción no válida")
            continue

        inv.registrarProducto(p)

    elif opc == "2":
        inv.mostrarInventario()

    elif opc == "3":
        codigo = input("Código del producto a vender: ")
        try:
            cantidad = int(input("Cantidad a vender: "))
        except:
            print("Cantidad inválida")
            continue

        inv.venderProducto(codigo, cantidad)

    elif opc == "4":
        codigo = input("Código: ")
        try:
            cantidad = int(input("Cantidad: "))
        except:
            print("Cantidad inválida")
            continue

        inv.reabastecer(codigo, cantidad)

    elif opc == "5":
        codigo = input("Código: ")
        inv.consultarProducto(codigo)

    elif opc == "6":
        print("Saliendo...")
        break

    else:
        print("Opción no válida")
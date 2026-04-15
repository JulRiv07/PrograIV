from services.inventario import Inventario
from models.computador import Computador
from models.celular import Celular
from models.accesorio import Accesorio

inv = Inventario()

while True:
    print("\n--- Menú Principal---")
    print("\n1. Registrar")
    print("2. Mostrar")
    print("3. Vender")
    print("4. Reabastecer")
    print("5. Consultar producto")
    print("6. Salir")

    opc = input("Opción: ")
    print("\n")

    if opc == "1":
        
        codigo = input("Código: ")
        nombre = input("Nombre: ")
        precio = float(input("Precio: "))
        if precio <= 0:
            print("Precio inválido")
            continue
        cantidad = int(input("Cantidad: "))
        if cantidad <= 0:
            print("Cantidad inválida")
            continue

        print("\n")
        tipo = input("Tipo \n1. computador\n2.celular\n3.accesorio\nOpción: ")
        print("\n")

        if tipo == "1":
            ram = input("RAM: ")
            cpu = input("CPU: ")
            p = Computador(codigo, nombre, precio, cantidad, ram, cpu)
        elif tipo == "2":
            alm = input("Almacenamiento: ")
            cam = input("Cámaras: ")
            p = Celular(codigo, nombre, precio, cantidad, alm, cam)
        elif tipo == "3":
            cat = input("Categoría: ")
            p = Accesorio(codigo, nombre, precio, cantidad, cat)
        else:
            print("Opción no válida")
            continue

        inv.registrar_producto(p)

    elif opc == "2":
        inv.mostrar_inventario()
    elif opc == "3":
        codigo = input("Código del producto a vender: ")
        cantidad = int(input("Cantidad a vender: "))
        inv.vender(codigo, cantidad)
    elif opc == "4":
        codigo = input("Código: ")
        cantidad = int(input("Cantidad: "))
        inv.rebastecer(codigo, cantidad)
    elif opc == "5":
        codigo = input("Código: ")
        inv.consultar_producto(codigo)
    elif opc == "6":
        print("Saliendo...")
        break
    else:
        print("Opción no válida")
        

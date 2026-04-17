import json
from Parcial2.Punto3.models.computador import Computador
from Parcial2.Punto3.models.celular import Celular
from Parcial2.Punto3.models.accesorio import Accesorio

def guardarProductos(productos):
    data = {}

    for cod, p in productos.items():
        info = {
            "tipo": p.__class__.__name__,
            "nombre": p.getNombre(),
            "precio": p.getPrecio(),
            "cantidad": p.getCantidad()
        }

        if info["tipo"] == "Computador":
            info["ram"] = p.ram
            info["procesador"] = p.procesador

        elif info["tipo"] == "Celular":
            info["almacenamiento"] = p.almacenamiento
            info["camaras"] = p.camaras

        elif info["tipo"] == "Accesorio":
            info["tipoAccesorio"] = p.tipo   

        data[cod] = info

    with open("Parcial2/Punto3/data/inventario.json", "w") as f:
        json.dump(data, f, indent=4)


def cargarProductos():
    try:
        with open("Parcial2/Punto3/data/inventario.json", "r") as f:
            data = json.load(f)

        productos = {}

        for cod, info in data.items():
            tipo = info["tipo"]

            if tipo == "Computador":
                p = Computador(
                    cod,
                    info["nombre"],
                    info["precio"],
                    info["cantidad"],
                    info.get("ram", ""),
                    info.get("procesador", "")
                )

            elif tipo == "Celular":
                p = Celular(
                    cod,
                    info["nombre"],
                    info["precio"],
                    info["cantidad"],
                    info.get("almacenamiento", ""),
                    info.get("camaras", 0)
                )

            else:
                p = Accesorio(
                    cod,
                    info["nombre"],
                    info["precio"],
                    info["cantidad"],
                    info.get("tipoAccesorio", "")
                )

            productos[cod] = p

        return productos

    except:
        return {}
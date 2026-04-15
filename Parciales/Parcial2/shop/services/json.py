import json
from models.computador import Computador
from models.celular import Celular
from models.accesorio import Accesorio

def guardar(productos):
    data = {}

    for cod, p in productos.items():
        info = {
            "tipo": p.__class__.__name__,
            "nombre": p.get_nombre(),
            "precio": p.get_precio(),
            "cantidad": p.get_cantidad()
        }

        if info["tipo"] == "Computador":
            info["ram"] = p.ram
            info["procesador"] = p.procesador

        elif info["tipo"] == "Celular":
            info["almacenamiento"] = p.almacenamiento
            info["camaras"] = p.camaras

        elif info["tipo"] == "Accesorio":
            info["categoria"] = p.categoria

        data[cod] = info

    with open("data/inventario.json", "w") as f:
        json.dump(data, f, indent=4)


def cargar():
    try:
        with open("data/inventario.json", "r") as f:
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
                    info.get("categoria", "")
                )

            productos[cod] = p

        return productos

    except:
        return {}
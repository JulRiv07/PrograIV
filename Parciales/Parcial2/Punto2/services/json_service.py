import json
from models import PacienteGeneral, PacientePrioritario, PacienteUrgencia

def guardarJSON(pacientes: list, archivo="pacientes.json"):
    datos = []
    for p in pacientes:
        base = {
            "tipo": type(p).__name__,
            "documento": p.documento,
            "nombre": p.nombre,
            "edad": p.edad,
            "estadoDeAtencion": p.estadoDeAtencion
        }
        if isinstance(p, PacienteGeneral):
            base["nombreEps"] = p.nombreEps
        elif isinstance(p, PacientePrioritario):
            base["condicionEspecial"] = p.condicionEspecial
        elif isinstance(p, PacienteUrgencia):
            base["nivelDeGravedad"] = p.nivelDeGravedad
        datos.append(base)
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=4)
    print(f"Datos guardados en {archivo}.")

def cargarJSON(archivo="pacientes.json") -> list:
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            datos = json.load(f)
        pacientes = []
        for d in datos:
            tipo = d["tipo"]
            if tipo == "PacienteGeneral":
                p = PacienteGeneral(d["documento"], d["nombre"], d["edad"],
                                    d["estadoDeAtencion"], d["nombreEps"])
            elif tipo == "PacientePrioritario":
                p = PacientePrioritario(d["documento"], d["nombre"], d["edad"],
                                        d["estadoDeAtencion"], d["condicionEspecial"])
            elif tipo == "PacienteUrgencia":
                p = PacienteUrgencia(d["documento"], d["nombre"], d["edad"],
                                     d["estadoDeAtencion"], d["nivelDeGravedad"])
            pacientes.append(p)
        print(f"Datos cargados desde {archivo}.")
        return pacientes
    except FileNotFoundError:
        print("Archivo no encontrado.")
        return []
import json
from Parcial2.Punto2.models import PacienteUrgencia, PacienteGeneral, PacientePrioritario

NIVELES = {"leve": 1, "moderado": 2, "grave": 3}

def _cargarDesdeJSON(archivo="Parcial2/Punto2/data/pacientes.json") -> list:
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
        return pacientes
    except FileNotFoundError:
        print("Error: no se encontró el archivo pacientes.json.")
        return []

def _pacienteMasCritico(pacientes: list):
    urgencias = [p for p in pacientes if isinstance(p, PacienteUrgencia)]
    if not urgencias:
        print("No hay pacientes de urgencias registrados.")
        return
    mas_critico = max(urgencias, key=lambda p: NIVELES.get(p.nivelDeGravedad.lower(), 0))
    print("\n--- PACIENTE MÁS CRÍTICO ---")
    print(mas_critico)

def menu_reportes():
    pacientes = _cargarDesdeJSON()  
    if not pacientes:
        print("No hay datos disponibles para generar reportes.")
        return

    while True:
        print("\n=============================")
        print("          REPORTES           ")
        print("=============================")
        print(f"  Pacientes cargados: {len(pacientes)}")
        print("=============================")
        print("1. Paciente más crítico")
        print("0. Volver al menú principal")
        print("=============================")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            _pacienteMasCritico(pacientes)
        elif opcion == "0":
            break
        else:
            print("Opción inválida. Intente de nuevo.")
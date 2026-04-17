from Parcial2.Punto2.models import PacienteUrgencia

def pacienteMasCritico(pacientes):
    
    niveles = {"leve": 1, "moderado": 2, "grave": 3, "crítico": 4}

    urgencias = [p for p in pacientes.pacientes if isinstance(p, PacienteUrgencia)]

    if not urgencias:
        print("No hay pacientes de urgencias registrados.")
        return

    mas_critico = max(urgencias, key=lambda p: niveles.get(p.nivelDeGravedad.lower(), 0))

    print("\n--- PACIENTE MÁS CRÍTICO ---")
    print(mas_critico)
from models import PacienteGeneral, PacientePrioritario, PacienteUrgencia
from services import guardarJSON, cargarJSON, pacienteMasCritico

def menu_reportes(sistema):
    while True:
        print("\n=============================")
        print("        REPORTES             ")
        print("=============================")
        print("1. Paciente más crítico")
        print("0. Volver al menú principal")
        print("=============================")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            pacienteMasCritico(sistema.pacientes)
        elif opcion == "0":
            break
        else:
            print("Opción inválida. Intente de nuevo.")


class Sistema:
    def __init__(self):
        self.pacientes = []

    def registrarPaciente(self, paciente):
        if self._documentoExiste(paciente.documento):
            print("Error: ya existe un paciente con este documento.")
            return False
        if not self._validarEdad(paciente.edad):
            print("Error: edad inválida.")
            return False
        self.pacientes.append(paciente)
        print(f"Paciente {paciente.nombre} registrado exitosamente.")
        return True

    def mostrarPacientes(self):
        if not self.pacientes:
            print("No hay pacientes registrados.")
            return
        for p in self.pacientes:
            print(p)

    def buscarPaciente(self, documento: int):
        for p in self.pacientes:
            if p.documento == documento:
                return p
        print(f"No se encontró ningún paciente con el documento {documento}.")
        return None

    def atenderSiguiente(self):
        orden = [PacienteUrgencia, PacientePrioritario, PacienteGeneral]
        for tipo in orden:
            for p in self.pacientes:
                if isinstance(p, tipo) and p.estadoDeAtencion != "Atendido":
                    p.estadoDeAtencion = "Atendido"
                    print(f"Paciente {p.nombre} atendido exitosamente.")
                    return True
        print("No hay pacientes pendientes.")

    def _documentoExiste(self, documento: int) -> bool:
        return any(p.documento == documento for p in self.pacientes)

    def _validarEdad(self, edad: int) -> bool:
        return 0 <= edad <= 120

#Menu

def registrar_paciente(sistema):
    print("\n--- REGISTRAR PACIENTE ---")
    print("1. General  2. Prioritario  3. Urgencias")
    tipo = input("Seleccione el tipo: ").strip().lower()
    try:
        documento = int(input("Documento: "))
        nombre = input("Nombre: ").strip()
        edad = int(input("Edad: "))
    except ValueError:
        print("Error: documento y edad deben ser números enteros.")
        return
    if tipo == "1" or tipo == "general":
        eps = input("Nombre de la EPS: ").strip()
        paciente = PacienteGeneral(documento, nombre, edad, "Pendiente", eps)
    elif tipo == "2" or tipo == "prioritario":
        condicion = input("Condición especial: ").strip()
        paciente = PacientePrioritario(documento, nombre, edad, "Pendiente", condicion)
    elif tipo == "3" or tipo == "urgencias":
        gravedad = input("Nivel de gravedad: ").strip()
        paciente = PacienteUrgencia(documento, nombre, edad, "Pendiente", gravedad)
    else:
        print("Tipo inválido.")
        return
    sistema.registrarPaciente(paciente)

def guardar_json(sistema):
    print("\n--- GUARDAR EN JSON ---")
    guardarJSON(sistema.pacientes)

def cargar_json(sistema):
    print("\n--- CARGAR DESDE JSON ---")
    confirmacion = input("¿Seguro? Los cambios no guardados se perderán (s/n): ").strip().lower()
    if confirmacion == "s":
        sistema.pacientes = cargarJSON()
    else:
        print("Carga cancelada.")

def mostrar_menu():
    print("\n=============================")
    print("   SISTEMA DE ATENCIÓN       ")
    print("         CLÍNICA             ")
    print("=============================")
    print("1. Registrar paciente")
    print("2. Mostrar todos los pacientes")
    print("3. Buscar paciente por documento")
    print("4. Atender siguiente paciente")
    print("5. Guardar en JSON")
    print("6. Cargar desde JSON")
    print("7. Reportes")
    print("0. Salir")
    print("=============================")

def main():
    sistema = Sistema()
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            registrar_paciente(sistema)
        elif opcion == "2":
            sistema.mostrarPacientes()
        elif opcion == "3":
            try:
                doc = int(input("Documento a buscar: "))
                p = sistema.buscarPaciente(doc)
                if p:
                    print(p)
            except ValueError:
                print("Error: el documento debe ser un número.")
        elif opcion == "4":
            sistema.atenderSiguiente()
        elif opcion == "5":
            guardar_json(sistema)
        elif opcion == "6":
            cargar_json(sistema)
        elif opcion == "7":
            menu_reportes(sistema)
        elif opcion == "0":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
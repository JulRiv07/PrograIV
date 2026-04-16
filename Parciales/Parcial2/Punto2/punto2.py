import json

#Clase Padre
class Paciente:
    def __init__(self, documento: int, nombre: str, edad: int, estadoDeAtencion: str):
        self.__documento = documento
        self.__nombre = nombre
        self.__edad = edad
        self.__estadoDeAtencion = estadoDeAtencion
    @property
    def documento(self):
        return self.__documento
    @documento.setter
    def documento(self, documento: int):
        self.__documento = documento
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre
    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad(self, edad: int):
        self.__edad = edad
    @property
    def estadoDeAtencion(self):
        return self.__estadoDeAtencion
    @estadoDeAtencion.setter
    def estadoDeAtencion(self, estadoDeAtencion: str):
        self.__estadoDeAtencion = estadoDeAtencion

    #Metodo de información
    def __str__(self):
        return f"Documento: {self.__documento}, Nombre: {self.__nombre}, Edad: {self.__edad}, Estado de atención: {self.__estadoDeAtencion}"

#Clase Hijo 1
class PacienteGeneral(Paciente):
    def __init__(self, documento: int, nombre: str, edad: int, estadoDeAtencion: str, nombreEps: str):
        super().__init__(documento, nombre, edad, estadoDeAtencion)
        self.__nombreEps = nombreEps
    @property
    def nombreEps(self):
        return self.__nombreEps
    @nombreEps.setter
    def nombreEps(self, nombreEps: str):
        self.__nombreEps = nombreEps

    def __str__(self):
        return super().__str__() + f", Nombre de la EPS: {self.__nombreEps}"

    

#Clase Hijo 2
class PacientePrioritario(Paciente):
    def __init__(self, documento: int, nombre: str, edad: int, estadoDeAtencion: str, condicionEspecial: str):
        super().__init__(documento, nombre, edad, estadoDeAtencion)
        self.__condicionEspecial = condicionEspecial
    @property
    def condicionEspecial(self):
        return self.__condicionEspecial
    @condicionEspecial.setter
    def condicionEspecial(self, condicionEspecial: str):
        self.__condicionEspecial = condicionEspecial

    def __str__(self):
        return super().__str__() + f", Condicion especial: {self.__condicionEspecial}"

#Clase Hijo 3
class PacienteUrgencia(Paciente):
    def __init__(self, documento: int, nombre: str, edad: int, estadoDeAtencion: str, nivelDeGravedad: str):
        super().__init__(documento, nombre, edad, estadoDeAtencion)
        self.__nivelDeGravedad = nivelDeGravedad
    @property
    def nivelDeGravedad(self):
        return self.__nivelDeGravedad
    @nivelDeGravedad.setter
    def nivelDeGravedad(self, nivelDeGravedad: str):
        self.__nivelDeGravedad = nivelDeGravedad
    
    def __str__(self):
        return super().__str__() + f", Nivel de gravedad: {self.__nivelDeGravedad}"

#Clase de base de datos para el sistema:
class Sistema:
    def __init__(self):
        self.pacientes = []

    #Funcionamiento del sistema
    def registrarPaciente(self, paciente: Paciente):
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
            print("No hay pacientes registrados en el sistema.")
            return
        for p in self.pacientes:
            print(p)

    def buscarPaciente(self, documento: int):
        for p in self.pacientes:
            if p.documento == documento:
                return p
        print(f"No se encontro ningun paciente con el documento {documento}.")
        return None
#Prioridad del sistema segun el documento del parcial: urgencias > priori > generales.
    def atenderPaciente(self):
        orden = [PacienteUrgencia, PacientePrioritario, PacienteGeneral]
        for tipo in orden:
            for p in self.pacientes:
                if isinstance(p, tipo) and p.estadoDeAtencion != "Atendido":
                    p.estadoDeAtencion = "Atendido"
                    print(f"Paciente {p.nombre} atendido exitosamente.")
                    return True
        print("No hay pacientes pendientes.")

    #Validaciones
    def _documentoExiste(self, documento: int) -> bool:
        return any(p.documento == documento for p in self.pacientes)
    
    def _validarEdad(self, edad: int) -> bool:
        return 0 <= edad <= 120
    
    #Guardar en JSON
    def guardarJSON(self, archivo="pacientes.json"):
        datos = []
        for p in self.pacientes:
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

    # 7. Leer desde JSON
    def cargarJSON(self, archivo="pacientes.json"):
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                datos = json.load(f)
            self.pacientes = []
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
                self.pacientes.append(p)
            print(f"Datos cargados desde {archivo}.")
        except FileNotFoundError:
            print("Archivo no encontrado.")

    
            
    
    
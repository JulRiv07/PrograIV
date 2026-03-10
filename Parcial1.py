class Empleados:
    def __init__(self, nombre, ID, salario, años_experiencia):
        self.nombre = nombre
        self.ID = ID
        self.salario = salario
        self.años_experiencia = años_experiencia
    def calcular_salario(self):
        if self.años_experiencia >= 0 and self.años_experiencia <=2:
            return (self.salario * 0.05) + self.salario
        elif self.años_experiencia >= 3 and self.años_experiencia <=5:
            return (self.salario * 0.10) + self.salario
        elif self.años_experiencia > 5:
            return (self.salario * 0.15) + self.salario
        
    def __str__(self):
        return f"Nombre: {self.nombre}, ID: {self.ID}, Salario: {self.salario}, Años de experiencia: {self.años_experiencia}"  
    
    class GestorEmpleados:
        def __init__(self):
            self.empleados = []
        def agregar_empleado(self, empleado):
            self.empleados.append(empleado)
        def eliminar_empleado(self, ID):
            for empleado in self.empleados:
                if empleado.ID == ID:
                    self.empleados.remove(empleado)
                    return True
            return False
    
        def buscar_empleado(self, ID):
            for empleado in self.empleados:
                if empleado.ID == ID:
                    return empleado
            return None
        
        def editar_empleado(self, ID, nombre=None, salario=None, años_experiencia=None):
            empleado = self.buscar_empleado(ID)
            if empleado:
                if nombre:
                    empleado.nombre = nombre
                if salario:
                    empleado.salario = salario
                if años_experiencia:
                    empleado.años_experiencia = años_experiencia
                return True
            return False
        
        def mostrar_empleados(self):
            for empleado in self.empleados:
                print(empleado)
        def guardar_empleados(self):
            with open("empleados.txt", "w") as file:
                for empleado in self.empleados:
                    file.write(f"{empleado.nombre},{empleado.ID},{empleado.salario},{empleado.años_experiencia}\n")
        def cargar_empleados(self):
            try:
                with open("empleados.txt", "r") as file:
                    for line in file:
                        nombre, ID, salario, años_experiencia = line.strip().split(",")
                        empleado = Empleados(nombre, ID, float(salario), int(años_experiencia))
                        self.agregar_empleado(empleado)
            except FileNotFoundError:
                print("No se encontró el archivo.")

def menu_empleados():
    gestor = Empleados.GestorEmpleados()
    gestor.cargar_empleados()

    while True:
        print("\nSistema de Gestión de Empleados")
        print("1. Agregar empleado")
        print("2. Eliminar empleado")
        print("3. Buscar empleado por ID")
        print("4. Mostrar empleados")
        print("5. Guardar empleados")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            ID = input("ID: ")
            salario = float(input("Salario: "))
            años = int(input("Años de experiencia: "))

            empleado = Empleados(nombre, ID, salario, años)
            gestor.agregar_empleado(empleado)
            print("Empleado agregado correctamente.")

        elif opcion == "2":
            ID = input("Ingrese el ID del empleado a eliminar: ")
            if gestor.eliminar_empleado(ID):
                print("Empleado eliminado.")
            else:
                print("Empleado no encontrado.")

        elif opcion == "3":
            ID = input("Ingrese el ID a buscar: ")
            empleado = gestor.buscar_empleado(ID)

            if empleado:
                print("\nEmpleado encontrado:")
                print(empleado)
                print("Salario con aumento:", empleado.calcular_salario())
            else:
                print("Empleado no encontrado.")

        elif opcion == "4":
            print("\nLista de empleados:")
            gestor.mostrar_empleados()

        elif opcion == "5":
            gestor.guardar_empleados()
            print("Empleados guardados en archivo.")

        elif opcion == "6":
            gestor.guardar_empleados()
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")


menu_empleados()
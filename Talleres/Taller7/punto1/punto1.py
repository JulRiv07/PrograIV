import math

class Figura:
    def calcular_area(self):
        def calcular_area(self):
            pass

class Triangulo(Figura):
    def __init__(self, base, altura):
        self.set_base(base)
        self.set_altura(altura)
    
    def set_base(self, base):
        if base > 0:
            self.__base = base 
        else:
            raise ValueError("La base debe ser un número positivo.")
        
    def set_altura(self, altura):
        if altura > 0:
            self.__altura = altura 
        else:
            raise ValueError("La altura debe ser un número positivo.")
        
    def calcular_area(self):
        return (self.__base * self.__altura) / 2
    

class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.set_ancho(ancho)
        self.set_alto(alto)
    
    def set_ancho(self, ancho):
        if ancho > 0:
            self.__ancho = ancho 
        else:
            raise ValueError("El ancho debe ser un número positivo.")
        
    def set_alto(self, alto):
        if alto > 0:
            self.__alto = alto 
        else:
            raise ValueError("El alto debe ser un número positivo.")
        
    def calcular(self):
        return self.__ancho * self.__alto
    
class Circulo(Figura):
    def __init__(self, radio):
        self.set_radio(radio)
    
    def set_radio(self, radio):
        if radio > 0:
            self.__radio = radio 
        else:
            raise ValueError("El radio debe ser un número positivo.")
        
    def calcular_area(self):
        return math.pi * (self.__radio ** 2)

class Trapecio(Figura):
    def __init__(self, base_mayor, base_menor, altura):
        self.set_base_mayor(base_mayor)
        self.set_base_menor(base_menor)
        self.set_altura(altura)

    def set_base_mayor(self, base_mayor):
        if base_mayor > 0:
            self.__base_mayor = base_mayor 
        else:
            raise ValueError("La base mayor debe ser un número positivo.")

    def set_base_menor(self, base_menor):   
        if base_menor > 0:
            self.__base_menor = base_menor 
        else:
            raise ValueError("La base menor debe ser un número positivo.")  

    def set_altura(self, altura):
        if altura > 0:
            self.__altura = altura 
        else:
            raise ValueError("La altura debe ser un número positivo.")  

    def calcular_area(self):      
        return ((self.__base_mayor + self.__base_menor) * self.__altura) / 2

def menu1():
    while True:
        print("\nCalculadora de Áreas")
        print("1. Triángulo")
        print("2. Rectángulo")
        print("3. Círculo")
        print("4. Trapecio")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")
    
        try:
            if opcion == "1":
                base = float(input("Ingrese base: "))
                altura = float(input("Ingrese altura: "))
                figura = Triangulo(base, altura)
                print("Área:", figura.calcular_area())

            elif opcion == "2":
                ancho = float(input("Ingrese ancho: "))
                alto = float(input("Ingrese alto: "))
                figura = Rectangulo(ancho, alto)
                print("Área:", figura.calcular_area())

            elif opcion == "3":
                radio = float(input("Ingrese radio: "))
                figura = Circulo(radio)
                print("Área:", figura.calcular_area())

            elif opcion == "4":
                base_mayor = float(input("Base mayor: "))
                base_menor = float(input("Base menor: "))
                altura = float(input("Altura: "))
                figura = Trapecio(base_mayor, base_menor, altura)
                print("Área:", figura.calcular_area())

            elif opcion == "5":
                print("bye bye :)")
                break
            
            else:
                print("Opción no válida. Intente nuevamente.")
        
        except ValueError as e:
            print("Error:", e)

if __name__ == "__main__":
    menu1()
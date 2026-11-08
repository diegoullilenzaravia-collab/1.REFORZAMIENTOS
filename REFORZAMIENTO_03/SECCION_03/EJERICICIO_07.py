
import math

# Crear la clase Circulo
class Circulo:

    # Constructor
    def __init__(self, radio):
        self.radio = radio

    # Método para calcular el área
    def calcular_area(self):
        if isinstance(self.radio, (int, float)) and self.radio > 0:
            area = 3.1416 * (self.radio ** 2)
            return area
        else:
            print("Error: El radio debe ser un número mayor que cero.")
            return None

    # Método para calcular el perímetro
    def calcular_perimetro(self):
        if isinstance(self.radio, (int, float)) and self.radio > 0:
            perimetro = 2 * 3.1416 * self.radio
            return perimetro
        else:
            print("Error: El radio debe ser un número mayor que cero.")
            return None


# Crear tres objetos con diferentes radios
circulo1 = Circulo(3)
circulo2 = Circulo(5)
circulo3 = Circulo(7)

# Mostrar resultados del primer círculo
print("----- CIRCULO 1 -----")
print("Radio:", circulo1.radio)
print("Area:", circulo1.calcular_area())
print("Perimetro:", circulo1.calcular_perimetro())

# Mostrar resultados del segundo círculo
print("\n----- CIRCULO 2 -----")
print("Radio:", circulo2.radio)
print("Area:", circulo2.calcular_area())
print("Perimetro:", circulo2.calcular_perimetro())

# Mostrar resultados del tercer círculo
print("\n----- CIRCULO 3 -----")
print("Radio:", circulo3.radio)
print("Area:", circulo3.calcular_area())
print("Perimetro:", circulo3.calcular_perimetro())

# Probar validación
circulo4 = Circulo(-2)
print("\n----- VALIDACION -----")
circulo4.calcular_area()
circulo4.calcular_perimetro()
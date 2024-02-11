import math

class Circulo:
    def __init__(self, radio):
        self.validar_radio(radio)

    def validar_radio(self, radio):
        try:
            self.radio = float(radio)
        except ValueError:
            raise ValueError("Error: El radio debe ser un valor numérico.")

    def calcular_area(self):
        return math.pi * self.radio**2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

    def pedir_radio(self):
        while True:
            try:
                radio = float(input("Ingrese el radio del círculo: "))
                self.validar_radio(radio)
                break
            except ValueError as e:
                print(e)

# Instanciar la clase dos veces y mostrar resultados
circulo1 = Circulo(5)  # Ejemplo con un radio predefinido
circulo2 = Circulo(8.5)  # Otro ejemplo con un radio predefinido

circulo1.pedir_radio()  # Solicitar radio al usuario para la primera instancia
circulo2.pedir_radio()  # Solicitar radio al usuario para la segunda instancia

# Mostrar resultados por consola
print("\nResultados para el círculo 1:")
print(f"Área: {circulo1.calcular_area()}")
print(f"Perímetro: {circulo1.calcular_perimetro()}")

print("\nResultados para el círculo 2:")
print(f"Área: {circulo2.calcular_area()}")
print(f"Perímetro: {circulo2.calcular_perimetro()}")


"""Crear una clase llamada círculo que contenga radio en su constructory
que contenga un método área que devuelva el área de un círculo.
Aplicar excepciones en caso no se ingrese un dato tipo numérico.
Crear adicionalmente un método que devuelva el perímetro del círculo.
Instanciar la clase respectivamente para dos diferentes radios.
Habrá un método donde pedirá el radio del círculo.
Instanciar mínimo 2 veces la clase y mostrar resultados por consola."""

class Circulo:
    pi = 3.14
    def __init__(self,radio):

       self.radio = radio

    def calcular_area(self):
        area = (self.radio ** 2) * Circulo.pi
        return area

    def calcular_perimetro(self):
        perimetro = 2 * Circulo.pi * self.radio
        return perimetro

    def pedir_radio(self):
        while True:
            try :
                self.radio = float(input("Ingrese el radio: "))
                break

            except ValueError:
                print("El radio ingresado no es un dato de tipo numerico")


radio1 = Circulo(5)
radio2 = Circulo(5)

radio1.pedir_radio()
print("el area del primer circula es {}".format(radio1.calcular_area()))
print("el perimetro del primer circulo es {}".format(radio1.calcular_perimetro()))

radio2.pedir_radio()
print("el area del segundo circula es {}".format(radio1.calcular_area()))
print("el perimetro del segundo circulo es {}".format(radio1.calcular_perimetro()))





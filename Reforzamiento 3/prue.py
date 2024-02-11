"""Escribir una clase en Python que contenga un método que convierta un
número entero en su cubo y contenga otro método que obtenga el
cuadrado de ese resultado. El valor inicial de resultado deberá estar
creado en el constructor. Considerar un método en la cual le pedirá al
usuario ingresar un valor numérico."""

class Metodo:
    def __init__(self):
        self.resultado = 0

    def valor(self):
       self.numero = int(input("ingrese un numero:"))

    def cubo(self):
        self.numero = self.numero ** 3

    def cuadrado(self):
        self.numero = self.numero ** 2

    def resultado_final(self):
        self.resultado = self.numero
        return self.numero

cantidad = Metodo()
cantidad.valor()
cantidad.cuadrado()
cantidad.cubo()


print("el resultado fianl es {}".format(cantidad.resultado_final()))

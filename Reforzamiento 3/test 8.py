"""Crear una clase que contenga dos métodos, uno que pida ingresar un
nombre y apellido, un método para pedir su edad y otro método que lo
imprima ambos resultados, pero estarán contenidos en un diccionario.
Comprobar ambos métodos instanciado la clase respectivamente.
Considerar en el constructor los valores necesarios."""

class Datos:
    def __init__(self,):
        self.diccionario = {"nombre":"","apellido":"","edad":""}


    def consultar_nombre_apellido(self):

        self.nombre = input("Ingrese el nombre: ")
        self.diccionario["nombre"] = self.nombre

        self.apellido = input("Ingrese el apellido: ")
        self.diccionario["apellido"] = self.apellido

    def consultar_edad(self):
        self.edad = int(input("Ingrese la edad: "))
        self.diccionario["edad"] = self.edad

    def imprimir(self):
        print("{} {} tiene {} años".format(self.nombre,self.apellido,self.edad))

    def mostrar_diccionario(self):
        print(self.diccionario)


persona1 = Datos()
persona2 = Datos()

persona1.consultar_nombre_apellido()
persona1.consultar_edad()
persona1.mostrar_diccionario()

persona2.consultar_nombre_apellido()
persona2.consultar_edad()
persona2.mostrar_diccionario()
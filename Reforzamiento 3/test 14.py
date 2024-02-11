"""Crear un módulo y un archivo principal (donde llamará las funciones del
módulo) el módulo tendrá una función para ingresar nombres y
apellidos, una función para pedir el tipo de seguro que tiene y otra
función para indicar si es mayor de edad o no (pedir la edad desde
consola)"""

class Modulo:
    def __init__(self):
        self.nombre = input("Ingrese el nombre: ")
        self.apellido = input("Ingrese el apellido: ")

    def pedirseguro(self):
        self.seguro = input("Ingrese el tipo de seguro que tiene: ")

    def pediredad(self):
        self.edad = int(input("Ingrese la edad: "))
        if self.edad >= 18:
            print( "{} es mayor de edad".format(self.nombre))
        else:
            print("{} es menor de edad".format(self.nombre))

class Archivoprincipal(Modulo):
    def archivo(self):
        print("archivo")

archivo1 = Archivoprincipal()

archivo1.pedirseguro()
archivo1.pediredad()
"""Creando un archivo principal (main.py) donde importará a un módulo
(operaciones.py) el cuál contendrá las siguientes funciones:

- Una función que realizará la carga de un valor entero.
- Una función que mostrará por pantalla la raíz cuadrada de dicho
valor
- Y otra función el valor elevado al cuadrado y al cubo de dicho
número.
- Utilizar el módulo math de python."""


from math import sqrt

def pedir_numero():

    while True:
        try:
            numero = int(input("Ingrese un numero: "))
            return numero
            break

        except ValueError:
            print("El valor ingresado no es numerico....")

def raiz_cuadrada(numero):
    return sqrt(numero)

def cuadrado_cubo(numero):
    return numero ** 2 , numero ** 3



"""Crear una función que sume los dígitos del número ingresado y
muestre por consola la suma de estos dígitos."""

def sumadigitos(numero):

    suma = 0
    for i in str(numero):
        suma = suma + int(i)

    return suma

numero = int(input("Ingreso el numero el cual se sumaran sus digitos: "))
print("La suma de digitos de {} es {}".format(numero, sumadigitos(numero)))
"""Pedir dos números positivos mediante terminal al usuario. Mostrar
como salida el número cuya sumatoria de dígitos es el mayor y los
números cuya sumatoria de dígitos es menor que 10. Utilizar una o
más funciones, según sea conveniente."""


# Funcion que suma los digitos
def sumadigitos(numero):

    suma = 0
    for i in str(numero):
        suma = suma + int(i)

    return suma


# pedir los números
numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))


if sumadigitos(numero1) > sumadigitos(numero2):
    print("El numero con mayor suma de digitos es {}".format(numero1))
elif sumadigitos(numero2) > sumadigitos(numero1):
    print("El numero con mayor suma de digitos es {}". format(numero2))
else:
    print("Los numeros tienen igual suma de digitos")

# lista de los numeros ingresados
numeros = [numero1, numero2]

# lista de numeros con suma de digitos menores a 10
lista_menores = []

# se usa "enumerate" para verficiar el (indice, valor) de la secuencia dejada por la funcion "map()"
for i, suma in enumerate(map(sumadigitos, numeros)):
    if suma < 10:
        lista_menores.append(numeros[i])


print("la lista de numeros con suma de digitos menores a 10 es: {}".format(lista_menores))

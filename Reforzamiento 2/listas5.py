#Ejercicio 19
"""Crea una lista vacía (con 10 posiciones), pedir al usuario c/u sus valores y que
finalmente se devuelva la suma y la media de los números ingresados de la lista."""

lista = []

for a in range(10):

    num = int(input("Ingrese el numero a la lista: "))

    lista.append(num)

print(lista)

suma = 0

for b in lista:

    suma = suma + b

promedio = suma / len(lista)

print("La suma de los elementos de la lista es {}".format(suma))
print("la media de los numeros es {}".format(promedio))

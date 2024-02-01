#Ejercicio 18
"""Crear una lista con los 15 primeros números impares, luego agregar 3 números flotantes
repetidos (los cuales son impares dentro del rango indicado y que no sea el último
impar).
- Empezando desde 1 y no 0.
- Agregar un cadena en la posición 3 de la lista.
- Eliminar este valor string de la cadena usando del."""

impares = []
for a in range(1,16):

    numero = (2*a)-1

    impares.append(numero)

print("los numeros impares son: {}".format(impares))

impares.insert(0,13.0)
impares.insert(1,13.0)
impares.insert(2,13.0)

impares.insert(3,"cadena")

print("La lista actualizada es: {}".format(impares))

del impares[3]

print("La lista final es: {}".format(impares))
"""Identificar que tipo de dato se obtiene al elevar un número a la exponente de 5 y
luego dividirlo por 10. Mostrar el resultado en pantalla."""

numero = int(input("Ingrese el numero: "))

exponente = (pow(numero,5)) / 10

print("El dato ‘{}’ es de tipo {}".format(exponente,type(exponente)))

"""Crear una función y dentro la respectiva excepción para el siguiente
bloque de código para que tu programa no se bloquee y además
imprime un mensaje al usuario la causa y/o solución:
lista = [2, 6, 10, 4, 5, 23, 1]
lista[10]"""


def detectar_error():

    lista = [2, 6, 10, 4, 5, 23, 1]

    try:

        print(lista[10])

    except IndexError:
        print("El dato pedido no esta en el rango establecido")


detectar_error()
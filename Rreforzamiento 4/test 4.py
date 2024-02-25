"""Crear una función y dentro la respectiva excepción para el siguiente
bloque de código para que tu programa no se bloquee y además
imprime un mensaje al usuario la causa y/o solución:
string = "Hello Pythonista"
print(string/0)"""


def detectar_error():

    string = "Hello Pythonista"

    try:

        print(string/0)

    except TypeError:
        print("No se puede realizar divisones entres datos tipo string y numericos, ni se puede realizar una divsion entre 0")




detectar_error()

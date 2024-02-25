"""Crear una función y dentro la respectiva excepción para el siguiente
bloque de código para que tu programa no se bloquee y además
imprime un mensaje al usuario la causa y/o solución:
persona= { 'nombre':'Xavier', 'apellido':'Rodriguez', 'dni':'63325345'}
persona['profesion']"""


def detectar_error():

    persona = {'nombre': 'Xavier', 'apellido': 'Rodriguez', 'dni': '63325345'}

    try:

        persona['profesion']

    except KeyError:
        print("La key que se esta pidiendo no existe")


detectar_error()

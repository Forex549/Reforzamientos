"""Crear una función para encontrar el error en el siguiente bloque de
código. Crea una excepción para evitar que tu programa se bloquee y
además imprime un mensaje al usuario la causa y/o solución:
suma = 80 + “Hola Pythonista”"""


def detectar_error():
        
    try:
        suma = 80 + "Hola Pythonista"
        print(suma)

    except TypeError:
        print("No se puede sumar datos numericos con strings")


detectar_error()

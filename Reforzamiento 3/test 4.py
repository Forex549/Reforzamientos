"""Pedir al usuario que ingrese una oración con un mínimo de 3 palabras
la cual será usada por parámetro para una función que se creará e
indicará cuantas palabras existen dentro de la oración ingresada."""

def contador(oracion):

    suma = 1
    oracion = oracion.rstrip()

    for i in oracion:
        if i == " ":
            suma = suma + 1

    return suma

oracion = input("Ingrese una oracion con minimo 3 palabras: ")

if contador(oracion) < 3:
    print("la oracion ingresada tienem menos de 3 palabras")
else:
    print("la oracion tiene {} palabras".format(contador(oracion)))


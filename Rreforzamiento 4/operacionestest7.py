"""Creando un archivo principal (main.py) donde importará a un módulo
(operaciones.py) el cuál contendrá las siguientes funciones:
- Una función que genere 30 números enteros aleatorios entre 0 y
100, que muestre en pantalla esta lista.
- Otra función que ordene los valores de una lista y volver a
mostrarla.
"""

import random

def generador():

    i = 0
    lista = []
    while i < 30:
        numero = random.randint(0,100)
        lista.append(numero)
        i = i + 1

    return lista

def ordenar(lista):
    return sorted(lista)
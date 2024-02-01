"""Usando la condicional if imprimir por pantalla si una lista está vacía o no, probar con
una lista vacía y otra con una lista vacía."""

lista = [1,2,3,4,5,6,7,8]

lista_2 = []

if len(lista) == 0:
    print("La lista esta vacia")
elif len(lista) >= 1:
    print("La lista no esta vacia")

if len(lista_2) == 0:
    print("La lista_2 esta vacia")
elif len(lista_2) >= 1:
    print("La lista_2 no esta vacia")
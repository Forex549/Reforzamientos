"""Crear una función que aceptará por parámetro dos valores que serán
ingresados por el usuario, una lista donde los valores serán llenados
por el usuario también y un segundo parámetro que eliminará de la
lista que fue ingresada a la función, finalmente el output de la función
será la lista actualizada sin el valor que se sacará de la lista. Mostrar
también la lista original y el número que fue eliminado."""

# Se crea la funcion que eliminara el valor que se ingrese de la lista
def eliminar(lista, elemento_eliminar):

    nueva_lista = []

    for i in lista:
        if i != elemento_eliminar:
            nueva_lista.append(i)
        else:
            continue

    return nueva_lista

# Se crea la lista inicial
lista_inicial = []

# Se llena la lista y se pide el valor que se eliminara
cantidad = int(input("Ingrese cuantos valores tendra la lista: "))

for a in range(cantidad):
    valor = int(input("Ingrese valor: "))
    lista_inicial.append(valor)

valor_eliminado = int(input("Ingrese el valor que desea eliminiar: "))

# Se muestran los resultados
print("La lista original es {}".format(lista_inicial))
print("El valor eliminado es {}".format(valor_eliminado))
print("la nueva lista es {}".format(eliminar(lista_inicial,valor_eliminado)))











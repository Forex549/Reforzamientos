#Ejercicios desde el 10 al 14

lista_1 = [5,9,51.9,45,20,16.6,89]

print("la lista es: {} ".format(lista_1))

lista_1.sort()

print("la lista ordenada es: {}".format(lista_1))

lista2 = [45.6,89.4,True,75.2,False,5.4]

print("la lista2 es: {}".format(lista2))
print("el penultimo y ultimo elemento de lista2 son {} y {}".format(lista2[4],lista2[5]))

lista_valores = []
lista2_valores = []

for a in lista_1:

    lista_valores.append(type(a))

for b in lista2:

    lista2_valores.append(type(b))

print("Los tipos de datos de la primera lista(`lista´) son: {}".format(lista_valores))
print("Los tipos de datos de la primera lista(`lista2´) son: {}".format(lista2_valores))

lista2.clear()

if len(lista2) > 0:
    print("La lista2 no esta vacía")
else:
    print("La lista2 esta vacía")

del lista_1[2]
del lista_1[0]

print("Finalmente la  lista_1 es: {} ".format(lista_1))
print("Fianlmente la lista_2 es: {} ".format(lista2))
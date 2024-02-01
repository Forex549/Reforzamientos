#ejercicio del 15 al 17

enteros = []

for a in range(1,101):
    enteros.append(a)

print(enteros)
print("los datos comprendidos entre la posicion 10 y 15 son: {}".format(enteros[10:35]))

cuadrados = []
for numero in enteros[0:10]:

    cuadrados.append(numero**2)
print("los primeros 10 numeros al cuadrado son: {}".format(cuadrados))
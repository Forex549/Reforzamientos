"""Crea una función que al ingresar dos números por parámetro mostrará
todos los cuadrados de los números que hay entre ellos (Usar la
función una vez y mostrar el resultado por consola). Los números
serán ingresados y solicitados al usuario."""

n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))


def funcion(n1, n2):

    list = []

    for i in range(n1+1, n2):
        list.append(i)

    list2 = []

    for a in list:
        elemento = a**2
        list2.append(elemento)

    return list2


print(funcion(n1, n2))

"""Crear una función donde se permitirá guardar el nombre, apellido y
edad de un usuario en un fichero (agenda.txt), cada usuario tiene que
estar guardado en una línea diferente y cada dato de una persona tiene
que estar separados por comas."""


def agregar_usuario():

    archivo = open("agenda.txt", "a")

    nombre = input("Ingrese el nombre del usuario: ")
    apellido = input("Ingrese el apellido del usuario: ")
    edad = int(input("Ingrese la edad del usuario: "))

    archivo.write("{}, {}, {} años\n".format(nombre, apellido, edad))

    archivo.close()


agregar_usuario()


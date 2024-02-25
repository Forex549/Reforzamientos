"""Crear una función que pida al usuario un número entero entre 1 y 20 y
guarde en un fichero (que no existe) con el nombre tabla.txt la tabla
de multiplicar de ese número, done n es el número introducido."""


def guardar_tabla_multiplicar():

    try:

        numero = int(input("Ingrese el numero: "))


        if numero >= 1 and numero <= 20:
            nuevo_archivo = open("tabla.txt", "w")

            for i in range(1, 21, 1):
                m = i * numero
                nuevo_archivo.write ("\n{} x {} = {}".format(numero, i, m))

            nuevo_archivo.close()


        else:
            print("El numero ingresado no eesta dentro del rango")

    except ValueError:
        print("Error Ingrese un valor numericio valido")


guardar_tabla_multiplicar()
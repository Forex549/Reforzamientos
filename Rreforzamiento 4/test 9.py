"""Crear una función que pida al usuario un número entero entre 1 y 20 y
guarde en un fichero (que no existe) con el nombre tabla.txt la tabla
de multiplicar de ese número, done n es el número introducido."""


def guardar_tabla_multiplicar():
    try:

        numero = int(input("Ingrese un número entero entre 1 y 20: "))

        if 1 <= numero <= 20:
            # Generar la tabla de multiplicar
            tabla = [f"{numero} x {i} = {numero * i}" for i in range(1, 11)]

            # Guardar la tabla en el archivo tabla.txt
            with open("tabla.txt", "w") as archivo:
                archivo.write("\n".join(tabla))

            print(f"La tabla de multiplicar del {numero} ha sido guardada en tabla.txt.")
        else:
            print("Error: El número ingresado no está en el rango válido.")

    except ValueError:
        print("Error: Ingrese un número entero válido.")


guardar_tabla_multiplicar()

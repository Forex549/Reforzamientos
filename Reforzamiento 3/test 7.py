"""Crear una clase en python que contenga un método que revierta una
cadena de palabras.
Input: "Hola Pythonista, seguimos adelante"
Output: "adelante seguimos Pythonista Hola"
Llamarlo mínimo 2 veces y mostrar el resultado por consola."""

class Palabra:
    def __init__(self,oracion):

        self.oracion = oracion

    def invertir(self):
        list = []
        self.oracion = self.oracion.rstrip()
        palabra = ""
        for i in self.oracion:

            if i != " ":
                palabra = palabra + i
            if i == " ":
                list.append(palabra)
                palabra = ""

        list.append(palabra)

        list.reverse()

        palabra_nueva = ""
        for a in list:
            palabra_nueva = palabra_nueva + a + " "

        return palabra_nueva


oracion1 = Palabra("Hola Pythonista")
oracion2 = Palabra("Hola mundo me voy a dormir")

print(oracion1.invertir())
print(oracion2.invertir())


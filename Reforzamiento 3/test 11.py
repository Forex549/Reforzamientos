"""Crear una clase Persona con los siguientes requerimientos.
La clase tendrá como atributos el nombre, edad y sueldo de una
persona. Implementar los métodos necesarios para inicializar los
atributos (constructor), un método para mostrar los datos e indicar si
la persona es mayor de edad o no y otro método que bonificación que
retornará el 20% adicional de su sueldo.
Instanciar por lo menos la clase con 2 diferentes personas.
"""
class Persona:
    def __init__(self, nombre, edad, sueldo):
        self.nombre = nombre
        self.edad = edad
        self.sueldo = sueldo

    def mmostrar_datos(self):
        print("Nombre: {}".format(self.nombre))
        print("Edad: {}".format(self.edad))
        print("Sueldo: {}".format(self.sueldo))

        if self.edad >= 18:
            print("{} es mayor de edad".format(self.nombre))
        else:
            print("{} es menor de edad".format(self.nombre))

    def calcular_bonificacion(self):
        bonificacion = self.sueldo * 0.2
        return bonificacion

persona1 = Persona("Jose", 18, 1300)
persona2 = Persona("Alvaro", 20, 2000)

persona1.mmostrar_datos()
print("la bonificacion de {} será {} soles".format(persona1.nombre, persona1.calcular_bonificacion()))

persona2.mmostrar_datos()
print("la bonificacion de {} será {} soles".format(persona2.nombre, persona2.calcular_bonificacion()))


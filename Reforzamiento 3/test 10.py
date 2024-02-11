"""Crear una clase llamada Alumno que tenga como atributos el nombre,
edad y la nota final del alumno. Crear los métodos para inicializar sus
atributos, otro para imprimirlos y un método para mostrar un mensaje
con el resultado de la nota y si ha aprobado (mayor o igual a 11) o no el
alumno.Instanciar la clase por lo menos 3 veces (3 alumnos)"""

class Alumno:

    def __init__(self, nombre, edad, nota_final):
        self.nombre = nombre
        self.edad = edad
        self.nota_final = nota_final

    def imprimirdatos(self):
        print("Nombre: {}".format(self.nombre))
        print("Edad: {}".format(self.edad))
        print("Nota: {}".format(self.nota_final))

    def resultadonota(self):
        if self.nota_final >= 11:
            print("la nota de {} es {} y ha aprobado".format(self.nombre, self.nota_final))
        else:
           print( "la nota de {} es {} y no ha aprobado".format(self.nombre, self.nota_final))


alumno1 = Alumno("Luis", 18, 11)
alumno2 = Alumno("Alejandro", 19, 8)
alumno3 = Alumno("Elizabeth", 19, 10)

alumno1.imprimirdatos()
alumno1.resultadonota()

alumno2.imprimirdatos()
alumno2.resultadonota()

alumno3.imprimirdatos()
alumno3.resultadonota()
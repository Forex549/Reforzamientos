"""12. Realizar una clase que administre una agenda. Se debe almacenar en
un diccionario dentro de una lista para cada contacto el nombre, el
teléfono, email y DNI. Deberá tener los siguientes métodos:

Añadir contacto
Mostrar contactos
Buscar contacto
(Por DNI)"""

class Agenda:
    def __init__(self):

        self.contactos = []
    def añadircontactos(self):

        diccionario = {}
        self.nombre = input("Ingrese el nombre del contacto: ")
        diccionario["nombre"] = self.nombre
        self.telefono = input("Ingrese el telfono del contacto:")
        diccionario["telefono"] = self.telefono
        self.email = input("Ingrese el emil del contacto: ")
        diccionario["email"] = self.email
        self.dni = input("Ingrese el dni del contacto: ")
        diccionario["dni"] = self.dni

        self.contactos.append(diccionario)

    def mostrarcontactos(self):
        print("Los contactos son:")
        for a in self.contactos:
            print(a)

    def buscarcontacto(self):

        personabuscar = input("Ingrese el nombre de la persona que deseaa buscar:")

        for i in self.contactos:
            if  i["nombre"] == personabuscar:
                print("El contacto {}  fue encontrado en la agenda".format(i["nombre"]))
            if i["nombre"] != personabuscar:
                print("El contacto no esta en la agenda")



agenda = Agenda()

agenda.añadircontactos()
agenda.añadircontactos()

agenda.mostrarcontactos()
agenda.buscarcontacto()
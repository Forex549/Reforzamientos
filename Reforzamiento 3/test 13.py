"""Crear una clase Persona que contenga dos atributos: nombre y edad.
Nombre y edad se ingresarán por teclado en el constructor.
Declarar una segunda clase llamada Empleado que herede de la clase
Persona y agregue un atributo sueldo y muestre si debe pagar
impuestos (10% es su sueldo-encapsulamiento) (sueldo superior a
4000)
Instanciar la clase Empleado, mostrar el sueldo del empleado y cuánto
debe pagar de impuesto."""

class Persona:
     def __init__(self):
         self.nombre = input("Ingrese el numbre: ")
         self.edad = int(input("Ingrese la edad: "))

class Empleado(Persona):

    def __init__(self, _sueldo):
        super().__init__()
        self._sueldo = _sueldo

    def verficiarimpuestos(self):
        if self._sueldo > 4000:
            impuesto = self._sueldo * 0.1
        else:
            impuesto = 0

        return impuesto

empleado1 = Empleado(4500)


print("{} tiene un sueldo de {}".format(empleado1.nombre, empleado1._sueldo))
print("{} con {} años debe pagar {} soles de impuesto".format(empleado1.nombre, empleado1.edad, empleado1.verficiarimpuestos()))



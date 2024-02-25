
def crear_archivo():

     open('calificaciones.txt', 'w')

def guardar_informacion():

    nombre = input('Ingrese el nombre del alumno: ')
    nota1 = int(input('Ingrese la primera nota: '))
    nota2 = int(input('Ingrese la segunda nota: '))
    promedio = (nota1 + nota2) / 2

    archivo = open('calificaciones.txt', 'a')

    archivo.write("{}, {}, {}, {}\n".format(nombre, nota1, nota2, promedio))

def comprobar_estado():
    archivo = open('calificaciones.txt', "r")
    buscar = input('Ingrese el nombre del alumno que deseas comprobar: ')
    lineas = archivo.readlines()

    encontrado = False

    for linea in lineas:
        dato = linea.split(",")
        nombre = dato[0]
        promedio = float(dato[3])

        if nombre == buscar:
            if promedio >= 11:
                print('El alumno {} aprobó'.format(nombre))
                encontrado = True
                break

            else:
                print('El alumno {} desaprobo.'.format(nombre))
                encontrado = True
                break

    if encontrado is False:
        print("El alumno no esta en el regsitro")

guardar_informacion()
guardar_informacion()
guardar_informacion()

comprobar_estado()






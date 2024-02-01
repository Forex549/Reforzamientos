
item = ["calculo", "biologia", "libros", "programacion", "laptop", "fisica"]

print("La primera lista es: {}".format(item))

nuevos_elementos = int(input("Ingrese cantidad de nuevo elementos: "))

for nuevos in range(0,nuevos_elementos):

    #Aqui se ingresan los nuevos elementos

    elmento = input("Ingrese nuevo elemento: ")

    #Aqui se agregan los nuevos elementos

    item.append(elmento)

print("La lista actualizada es: {}".format(item))

eliminar = int(input("Ingrese cantidad de elementos que desea eliminar: "))

for a in range(0,eliminar):

    eliminado = input("Ingrese elemento que desea eliminar")

    item.remove(eliminado)

print(item)
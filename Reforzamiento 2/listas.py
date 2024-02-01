#Ejercicio del numero 1 al 9


item = ["calculo","calculo", "biologia", "quimica", "fisica", "programacion", "estadistica", "fisica","fisica","programacion"]

print("La primera lista es: {}".format(item))

item.append("algoritmica")
item.append(5)
item.append("promedio")
item.append("electronica")

print("La nuea lsita es: {}".format(item))

item.remove("biologia")
item.remove("quimica")

item.reverse()

print("La lista actualizada es: {} tiene {} items en total".format(item, len(item)))

print("La cantidad que se repite 'programacion' y 'fisica' son {} y {} ".format(item.count("programacion"), item.count("fisica")))

del item[0]

nueva_lista = []

nueva_lista.append(15)
nueva_lista.append(26.35)
nueva_lista.append("laptop")
nueva_lista.append(78)

lista_final = item + nueva_lista

print("La lista final es: {}".format(lista_final))




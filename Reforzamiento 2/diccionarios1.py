
diccionario = {"nombre": "giancarlo", "edad": 19, "salario": 3000, "edad para un empleado": 20}
print("el diccionairo es: {}".format(diccionario))

lista_dic = list(diccionario)
print("El diccionario como lista es: {}".format(lista_dic))

list_datos = []
for datos in lista_dic:

    list_datos.append(type(datos))

print("los tipos de datos de la lista son: {}".format(list_datos))

diccionario["DNI"] = 73232344

del diccionario["edad"]

list_dic_acatual = list(diccionario)

tipos_dato_dicc = []

for a in list_dic_acatual:
    tipos_dato_dicc.append(type(a))

print("los tipos de datos final que tiene el diccionario son: {}".format(tipos_dato_dicc))

dict[("dato1", 1), ("dato2", 2), ("dato3", 3), ("dato4", 4)]

departamentos = {"Lima": "Lima", "Arequipa": "arequipa", "Cusco": "cusco", "Piura": "piura", "Junín": "Huancayo", "Ica": "Ica"}

del departamentos["Arequipa"]

list_departamentos = list(departamentos)

for verificar in list_departamentos:

    if verificar == "Arequipa":
        resultado = "Arequipa se encuentra en el diccionario"

    else:
        resultado ="Arequipa no se encuentra en el diccionario"

print(resultado)
print("los departamentos en el diccionario son {}".format(list_departamentos))

diccionario["Carrera"] = "Ing.Software"

print("El diccionario final del inicio es {}".format(diccionario))

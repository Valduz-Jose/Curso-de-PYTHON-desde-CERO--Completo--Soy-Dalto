diccionario = {
  "nombre": "Juan",
  "edad": 30,
  "apellido": "Pérez",
  "subs":1000000
}

#Devuelve un objeto iterable con las claves del diccionario
claves = diccionario.keys()
#keys sirve para obtener las claves de un diccionario e iterarlas

#Obteniendo un elemento con Get (si no encuentra nada el programa continua)
claves = diccionario.get("subs")
#get sirve para obtener el valor de una clave especifica

#elimiar todo el diccionario
#diccionario.clear()

#eliminar un elemento del diccionario
diccionario.pop("apellido")#usando coma puedo eliminar varios elementos

#Obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()
#items sirve para obtener las claves y valores de un diccionario e iterarlas  


print(diccionario)
lista = ["Lucas Dalto","Soy Dalto",True,1.85] #las listas son mutables (se pueden modificar)
tupla = ("Argentina","Uruguay","Brasil") #Las tuplas son inmutables (no se pueden modificar)

print(lista)
print(lista[1])
print(tupla[1])

#creando un conjunto (set)
conjunto = {"Venezuela","Cuba","Noruega","Argelia","Venezuela"} #los conjuntos no permiten elementos repetidos
print(conjunto)
#los elementos no se pueden modificar, pero se pueden agregar o eliminar elementos del conjunto
#no se puede acceder a un elemento por su indice porque no tienen orden
#no pueden tener elementos duplicados

#creando un diccionario
diccionario = {
    "nombre": "Dalto", #conjunto clave - valor
    "apellido": "Lucas",
    "edad": 30,
    "altura": 1.85,
    "esta_emocionado": True,
    "dato_duplicado":"Dalto"
} #los diccionarios son mutables y tienen pares clave-valor
print(diccionario)
print(diccionario["nombre"])

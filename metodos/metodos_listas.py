#Creando una lista con el constructor list
lista = list (["Hola","dalto","Chau"])

cadena = "hola"
resultado = len(lista) #devuelve la cantidad de elementos en la lista

#Agregando un elemento al final de la lista
lista.append("Jajajaja")
#Agregando un elemento en una posicion especifica
lista.insert(1,"Nuevo elemento")
#Agregando varios elementos al final de la lista
lista.extend(["elemento1","elemento2","elemento3"])
#Eliminando un elemento por su indice
lista.pop(2)
#Eliminar el ultimo elemento de la lista
lista.pop(-1)
#Eliminar un elemento por su valor
lista.remove("Hola")#si no encuentra el valor da error
#Eliminando todos los elementos de la lista
#lista.clear()
#Ordenar los elementos de la lista de forma ascendente
lista.sort() #si hay diferentes tipos de datos da error
#invierte el orden de los elementos en la lista
lista.reverse()

print (lista)
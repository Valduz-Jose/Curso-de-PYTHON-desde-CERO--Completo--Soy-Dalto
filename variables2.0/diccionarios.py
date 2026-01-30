#creando diccionarios con dict()
diccionario = dict(nombre="Lucas", apellido="Dalto")
#solo se pueden crear diccionarios vacios con dict() no con {}
#las listas no pueden ser claves
diccionario = {frozenset (["dato 1","dato 2"]):"jajajaj"}

#creando diccionario con fromkeys()
diccionario = dict.fromkeys (["nombre","apellido","suscriptores"])
#creando diccionario con fromkeys()
diccionario = dict.fromkeys (["nombre","apellido","suscriptores"],"sin dato")

print(diccionario)
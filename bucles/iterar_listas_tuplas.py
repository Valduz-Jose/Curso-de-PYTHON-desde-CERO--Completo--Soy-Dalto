#creo una lista de animales
animales = ["pez","perro", "gato", "conejo", "loro"]
numeros = [1, 2, 3, 4, 5]

#recooriendo la lista animales
for animal in animales:
  print("El animal es:", animal)
  
#recooriendo la lista numeros y multiplicando cada valor *10
for numero in numeros:
  resultado = numero * 10
  print("El numero por 10 es:", resultado)

#iterando 2 listas con zip()
for numero,animal in zip(numeros,animales):
  print(f'Recorriendo lista 1: {numero}')
  print(f'Recorriendo lista 2: {animal}')

#iterar usando range
for num in range(5,10):
  print("El numero es:", num)
#primer parametro es el inicio, el segundo es el fin(no incluido) y el tercero es el paso

#Forma correcta de recorrer una lista con su indice
for num in enumerate(numeros):
  indice = num[0]
  valor = num[1]
  print(f'El indice es: {indice}, y el valor es: {valor}' )
  
#USANDO el else
for numero in numeros:
  print(f"ejecutando el ultimo bucle, valr actual: {numero}")
else:
  print("El bucle termino")
  #el else se ejecuta cuando el bucle termina normalmente, sin interrupciones
  
  #todo lo anterior funciona exactamente igual con tuplas
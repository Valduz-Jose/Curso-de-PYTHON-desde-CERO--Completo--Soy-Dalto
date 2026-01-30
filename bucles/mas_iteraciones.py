#Lista con 7 frutas
frutas = ["manzana", "banana", "pera", "naranja", "kiwi", "mango", "uva"]
numeros = [1,2,3,4,5,6,7,8,9,10]

#evitando q se coma una fruta usando continue
for fruta in frutas:
  if fruta == "kiwi":
    continue
  print(f'Me voy a comer una {fruta}  ')

#evitar que el bucle siga ejecutandose
for fruta in frutas:
  print(f'Me voy a comer una {fruta}  ')
  if fruta == "naranja":
    break
else:
  print("Bucle terminado")

#recorrer una cadena de texto
cadena = "Hola soy una cadena de texto"

for letra in cadena:
  print(f'La letra actual es: {letra}')
  
#for en una sola linea de codigo
numeros_duplicados = [x * 2 for x in numeros]

print(numeros_duplicados)
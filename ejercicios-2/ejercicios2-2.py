#creando una funcion que devuelva los numeros primos entre 0 y el numero que se le pasa
#funcion q verifica si un numero es primo
def es_primo(num):
  for i in range(2,num-1):
    if num%i==0: return False
  return True

#funcion que devuelve una lista con los numeros primos hasta el numero que se le pasa
def primos_hasta(num):
  primos = []
  for i in range(3,num+1):
    resultado = es_primo(i)
    if resultado == True: primos.append(i)
  return primos

#probando la funcion
resultado = primos_hasta(13)
print(resultado)
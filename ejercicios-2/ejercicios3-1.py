#Mostar la serie de fibonacci desde el 0 hasta el numero que se le pase
def fibonacci(num):
  a,b = 0,1
  fibonacci_lista = [0]
  for i in range(num):
    if b > num: return fibonacci_lista
    else:
      fibonacci_lista.append(b)
      a,b = b,a+b

resultado = fibonacci(34)
print(resultado)
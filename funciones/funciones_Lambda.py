numeros = [1,2,3,4,5,6,7,8,9,10]

#lambda es una funcion anonima que puede tener cualquier numero de argumentos pero solo una expresion
#Hacen un retorno automatico de la expresion evaluada
multiplicar_por_dos = lambda x : x*2
print(multiplicar_por_dos(5)) #Salida: 10

#usando filter con una funcion comun
def es_par(num):
    if (num % 2 == 0):
        return True
numeros_pares = filter(es_par, numeros)
print(list(numeros_pares)) #Salida: [2, 4, 6

#creando lo mismo q antes pero con lambda
numeros_pares_lambda = filter(lambda numero: numero % 2 == 0, numeros)
print(list(numeros_pares_lambda)) #Salida: [2, 4, 6, 8, 10]
#filter recibe dos parametros, el primero es una funcion que devuelve True o False y el segundo es un iterable
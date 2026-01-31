#Built-in functions en Python

#Encontrando el numero mayor de una lista
numeros = [3, 5, 2, 8, 1]
numero_mas_alto = max(numeros)
print("El numero mas alto es:", numero_mas_alto)

#Encontrando el numero menor de una lista
numero_mas_bajo = min(numeros) 
print("El numero mas bajo es:", numero_mas_bajo)

#Redondeando un numero a 6 decimales
numero_decimal = 3.14159265359
numero_redondeado = round(numero_decimal, 6)
#Se le puede especificar la cantidad de decimales
print("Numero redondeado a 6 decimales:", numero_redondeado)

#funcion bool Retorna False -> 0, "", None, False
resultado_bool = bool(0)
print("El resultado booleano es:", resultado_bool)
#Retorna True -> Cualquier otro valor diferente a los anteriores
resultado_bool_verdadero = bool(5)
print("El resultado booleano es:", resultado_bool_verdadero)

#Funcion all Retorna True si todos los elementos son verdaderos
resultado_all = all([True, 1, "Hola"])
print("El resultado de all es:", resultado_all)

#Funcion sum Suma todos los elementos de una lista
suma_numeros = sum(numeros)
print("La suma de los numeros es:", suma_numeros)


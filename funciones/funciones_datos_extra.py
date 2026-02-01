#creando una funcion de 3 parametros posicionales 
def frase(nombre, apellido, adjetivo): #Los parametros son posicionales
  return f" Hola {nombre} {apellido}, sos muy {adjetivo}."

frase = frase("Juan", "Perez", "inteligente")
print(frase)

#creando la misma funcion pero con un parametro por defecto
def frase2(nombre, apellido, adjetivo="genial"): #El parametro adjetivo tiene un valor por defecto
  return f" Hola {nombre} {apellido}, sos muy {adjetivo}."

frase2 = frase2("Ana", "Gomez") #No es necesario pasar el parametro adjetivo
print(frase2)
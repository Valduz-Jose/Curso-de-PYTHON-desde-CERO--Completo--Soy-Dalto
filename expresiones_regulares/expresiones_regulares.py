import re

texto = '''Hola maestro, esta es la cadena 1. , como estas mi capitan
Esta es la segunda linea 253 de texto
y esta es la final definitiva linea 3 mi capitan'''
#Haciendo una busqueda simple
resultado = re.findall("esta",texto,flags=re.IGNORECASE)

# print(resultado)

#\d -> busca digitos numericos del 0 - 9
resultado = re.findall(r"\d",texto)
#\D busca todo menos digitos numericos del 0 - 9
resultado = re.findall(r"\D",texto)
#\w busca caracteres alfanumericos
resultado = re.findall(r"\w",texto)
#\W busca todo menos caracteres alfanumericos
resultado = re.findall(r"\W",texto)
#\s busca espacios en blanco,saltos en linea
resultado = re.findall(r"\s",texto)
#\S busca todo menos espacios en blanco,saltos en linea
resultado = re.findall(r"\S",texto)
#. busca todo menos saltos en linea
resultado = re.findall(r".",texto)
#\n busca saltos en linea
resultado = re.findall(r"\n",texto)
#\ cancelar caracteres especiales (en este caso el punto)
resultado = re.findall(r"\. ",texto)

#armando una cadena que busque un numero,seguido de un punto y un espacio
resultado = re.findall(f"\d\.\s",texto)

#Buscar comienzo de una linea (en este caso Hola)
resultado = re.findall(f'^Hola',texto)

#Buscar comienzo de una linea (en este caso Hola) en cada nueva linea
resultado = re.findall(f'^Esta',texto,flags=re.M)

#Busca al final d euna linea 
resultado = re.findall(r'capitan$',texto,flags=re.M)

#{n} -> busca n cantidad de veces el valor de la izquierda
resultado = re.findall(r'\d{3}\s',texto)

#{n,m} -> al menos n a lo mucho m
resultado = re.findall(r'\d{1,4}',texto)

#busca subconjuntos o grupos n veces
resultado = re.findall(r'(ab){1}',texto)

# | -> busca una cosa o la otra
resultado = re.findall(r'\d{1,4}|Hola',texto)

print(resultado)



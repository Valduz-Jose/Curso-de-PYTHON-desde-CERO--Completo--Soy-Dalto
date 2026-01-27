cadena1 = "hOla"
cadena2 = "Bienvenido maquinola"

#print(dir(cadena1))
#DIR devuelve todos los metodos que tiene un objeto

resultado = dir(cadena1)

#convierte a mayusculas
mayusc = cadena1.upper() #Se usa Dato.metodo()

#convierte a minusculas
minusc = cadena1.lower()

#Convierte la primera letra en mayuscula
primera_letra_mayusc = cadena1.capitalize()

#buscamos una cadena en otra cadena
busqueda_find = cadena1.find("soy") #Devuelve la posicion donde empieza la cadena buscada 
#muestra -1 si no la encuentra

#buscamos una cadena en otra cadena
busqueda_index = cadena1.index("h") #Devuelve la posicion donde empieza la cadena buscada
#si no encuentra la cadena lanza un error

#si es numerico devuelve true
es_numerico = cadena1.isnumeric()

#si es alfabetico devuelve true
es_alfabetico = cadena1.isalpha()

#contamos coincidencias de una cadena en otra y devuelve la cantidad de coincidencias
contar_coincidencias = cadena2.count("a")

#contamos caracteres de una cadena
contar_caracteres = len(cadena2)

#verifica si una cadena empieza con un caracter o cadena especifica
empieza_con = cadena2.startswith("B") #Devuelve True si empieza con el caracter buscado

#verifica si una cadena termina con un caracter o cadena especifica
termina_con = cadena2.endswith("a") #Devuelve True si termina con el caracter

#remmplaza un pedazo de la cadena dada por otra cadena
cadena_nueva = cadena2.replace("maquinola", "amigo")

#split divide una cadena en partes y las devuelve en una lista
cadena_separada = cadena2.split(" ") #Divide la cadena en cada espacio

print(cadena_separada)
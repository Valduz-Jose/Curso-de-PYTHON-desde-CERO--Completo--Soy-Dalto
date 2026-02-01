# #creando una funcion simple 
# def saludar():
#     print("Hola, bienvenido a Python")

# #Ejecutando la funcion
# saludar()

#Funcion con parametros
def saludar_persona(nombre, sexo):
  sexo = sexo.lower()
  if sexo == "mujer":
      adjetivo = "Princesa bienvenida"
  elif sexo == "hombre":
      adjetivo = "Rey bienvenido"
  else:
      adjetivo = "Crack bienvenid@"
  print(f"Hola {nombre}, mi {adjetivo} a Python")

#Ejecutando la funcion con argumentos
saludar_persona("Alejandro", "Hombre")
saludar_persona("Camila", "Mujer")

#Crear una funcion que retorne valores
def crear_contrasena_random(num):
  chars = "abcdefghij"
  num_entero = str(num) #Convertir a string para poder acceder a sus caracteres por indice
  num = int(num_entero[0])#Convertir de nuevo a entero para hacer operaciones 
  c1 = num -2
  c2 = num
  c3 = num -5
  contrasena = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
  return contrasena,num
 
#Desempaquetando los valores retornados
password,primer_numero = crear_contrasena_random(7)
frase = f"Tu contraseña es: {password} a base de el numero {primer_numero}"
print(frase)
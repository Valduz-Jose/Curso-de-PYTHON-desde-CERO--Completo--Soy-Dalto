#Usando Open para abrir archivos
archivo_sin_leer= open("archivos\\texto_de_dalto.txt",encoding="UTF-8")
# archivo=archivo_sin_leer.read()

#Leer lineas del archivo
# lineas = archivo_sin_leer.readlines()
#Cuando un archivo se lee se debe cerrar para poder volver a leerlo
#leer una sola linea
linea = archivo_sin_leer.readline()#si coloco un numero lee esa cantidad de caracteres
#cerrar el archivo
archivo_sin_leer.close()

print(linea)

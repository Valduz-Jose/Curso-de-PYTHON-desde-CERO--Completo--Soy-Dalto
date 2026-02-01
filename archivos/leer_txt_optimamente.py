#abriendo el archivo con with open
with open("archivos\\texto_de_dalto.txt",encoding="UTF-8") as archivo:
  print(archivo.read())
#no es necesario cerrarlo gracias a With open

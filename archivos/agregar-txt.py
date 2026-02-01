with open('archivos\\texto_de_dalto','a') as archivo:
  #Apend lo que hace es agregar al archivo
  #archivo.writelines(["Hola maestro como andas\n","misericordia\n"])
  for i in range (5):
    archivo.write(f"Linea {i+1} agregada \n")

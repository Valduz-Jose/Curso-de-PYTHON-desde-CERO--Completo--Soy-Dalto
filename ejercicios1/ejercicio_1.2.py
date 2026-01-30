frase = input("Ingrese una frase y te calculo cuanto demorarias diciendola: ")
palabras_separadas = frase.split(" ")
cantidad_de_palabras = len(palabras_separadas)
print(f'Dijiste  {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras /2} segundos en decirla')
print(f'Dalto lo diria en {cantidad_de_palabras *100 //2*1.3/100} segundos en decirlo')
if cantidad_de_palabras > 120:
    print("Esa es una frase muy larga")
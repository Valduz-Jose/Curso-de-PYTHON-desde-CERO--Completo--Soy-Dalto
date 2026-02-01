def suma(nombre,*numeros):#el args debe ser el ultimo parametro 
    return f"{nombre}, la suma de tus numeros es: {sum(numeros)}"
  
resultado = suma("Alejandro",3,5,9,1)
print( resultado)


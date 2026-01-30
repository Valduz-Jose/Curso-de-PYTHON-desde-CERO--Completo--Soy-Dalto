diccionario = {
  "nombre": "Lucas",
  "apellido": "Dalto",
  "subscriptores": 100000000
}

#recorriendo diccionario para obtener las claves y los valores
for key in diccionario:
    print(f'La clave es: {key}')
    
#recorriendo diccionario para obtener las claves y los valores
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f'La clave es: {key}, y el valor es: {value}')
    
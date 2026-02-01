#pedir el nombre y la edad de los compas de clase
def obtener_companeros(cantidad_compas):
    companeros = []
    for i in range(cantidad_compas):
        nombre = input("Ingrese el nombre del compañero: ")
        edad = input("Ingrese la edad de: ")
        companeros.append((nombre, edad))
    companeros.sort(key=lambda x: x[1])  # Ordenar por edad
    asistente = companeros[0][0]  # El más joven
    profesor = companeros[-1][0]  # El mayor
    return asistente, profesor

asistente,profesor = obtener_companeros(5)

print(f"El profesor es {profesor} y su asistente de clase es: {asistente}")
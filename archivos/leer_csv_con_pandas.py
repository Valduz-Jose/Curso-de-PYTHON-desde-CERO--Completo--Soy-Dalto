import pandas as pd

#usando la funcion read_csv
df = pd.read_csv("archivos\\datos.csv")
df2 = pd.read_csv("archivos\\datos.csv")
#puede usar esto para encabezado names = ["name","lastname","age"]

#obteniendo la columna nombre

print(df["nombre"])

cadena = "0123456789"
print(cadena[:3])#usando slaicing para definir desde donde y hasta donde

#ordenando el dataframe por edad
df_ordenado = df.sort_values("edad")
print(df_ordenado)

#ordenando de forma descendente
df_ordenado = df.sort_values("edad",ascending=False)
print(df_ordenado)

#Concatenando los dos dataframes
df_concatenado = pd.concat([df,df2])

#accediendo a la primera fila con head
primera_fila = df.head(1)
print(primera_fila)

#accediendo a las ultimas filas con tail

ultima_fila = df.tail(3)
print(ultima_fila)

#accediendo a la cantidad de filas y columnas con shape

filas_totales,columnas_totales = df.shape

#obteniendo data estadistica del dataframe
df_info = df.describe()

#accediendo a un elemento especifico del dataframe con loc
elemento_especifico_loc = df.loc[2,"edad"]
#accediendo a un elemento especifico del dataframe con iloc
elemento_especifico_loc = df.iloc[2,2]

#accediendo a todas las filas de una columna
apellidos = df.iloc[:,1]
#accediendo a la fila 3 con loc
fila_3 = df.loc[2,:]

#accediendo a filas comn edad mayor de 30
mayor_que_30 = df.loc[df["edad"]<30,:]

print(mayor_que_30)
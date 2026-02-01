#Cambiar el tipo de dato de una columna
import pandas as pd
df = pd.read_csv("archivos_problemas_resueltos\\datos.csv")

#convierte a string los datos de una columna
df['edad'] = df['edad'].astype(str)

#mostrar el tipo de dato del primer ellemento de la columna edad
print(type(df['edad'][0]))

#remplazando datos
df['apellido'].replace("dalto","maestro",inplace=True)

#eliminar filas con datos faltantes
df = df.dropna()
df = df.dropna(axis=1)#para eliminar columnas con datos faltantes

#eliminando filas repetidas
df = df.drop_duplicates()

#creando un csv con el dataframe limpo
df.to_csv("archivos_problemas_resueltos\\datos_limpios.csv")
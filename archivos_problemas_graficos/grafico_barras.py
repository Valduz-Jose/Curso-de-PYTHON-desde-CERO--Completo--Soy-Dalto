import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos_problemas_graficos\\cofla_ingresos.csv")
#creando un grafico
sns.barplot(x="fuente",y="ingresos",data=df)
total_ingresos = df['ingresos'].sum()
print(f"Total de Ingresos ${total_ingresos} USD")
plt.show()
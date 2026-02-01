import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos_problemas_graficos\\pedos.csv")
#creando un grafico
sns.lineplot(x="fecha",y="pedos",data=df)
#creando un punto en el mayor
plt.plot("26-01",20,"o")

plt.show()
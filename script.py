import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Cria o vetor x com números inteiros de -20 a 20
x = list(range(-20, 21))

# Cria o vetor y com os valores de x ao cubo
y = [i**3 for i in x]

# Cria o dataframe com as variáveis x e y
df = pd.DataFrame({'x': x, 'y': y})

# Cria o plot de dispersão
sns.scatterplot(data=df, x='x', y='y')

# Exibe o gráfico
plt.title("Dispersão de X e X^3")
plt.show()


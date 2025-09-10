import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/datasets/gdp/master/data/gdp.csv"
tabela = pd.read_csv(url)

# Filtrar apenas Brasil e selecionar alguns anos
brasil = tabela[tabela['Country Name'] == 'Brazil']
anos_escolhidos = brasil[brasil['Year'].isin([1995, 2005, 2015, 2020])]

# Gráfico de barras
plt.bar(anos_escolhidos['Year'], anos_escolhidos['Value'])
plt.title('PIB do Brasil em anos selecionados')
plt.xlabel('Ano')
plt.ylabel('PIB em USD')
plt.show()

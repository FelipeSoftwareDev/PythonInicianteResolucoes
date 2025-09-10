import pandas as pd

# URL pública de um CSV simples
url = "https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"

# Lendo o arquivo direto da web
tabela = pd.read_csv(url)

print(tabela.head())

# Mostra os registros finais da tabela
print(tabela.tail())

# Faz o Pandas mostrar todas as linhas sem limitar a exibição
pd.set_option('display.max_rows', None)

# Faz o Pandas mostrar todas as colunas
pd.set_option('display.max_columns', None)

# Agora o print mostrará a tabela inteira
print(tabela)

import matplotlib.pyplot as plt

# URL com dados de PIB de países
url = "https://raw.githubusercontent.com/datasets/gdp/master/data/gdp.csv"

# Lendo os dados
tabela = pd.read_csv(url)

# Pegando apenas os dados do Brasil
brasil = tabela[tabela['Country Name'] == 'Brazil']

# Criando gráfico de linha com Matplotlib, passando o ano (year) como eixo x, PIB(value) como eixo y e marker apenas para marcar com pontos cada ano.
plt.plot(brasil['Year'], brasil['Value'], marker='o')

# Title como o nome sugere indica o título do Gráfico
plt.title('PIB do Brasil (1989 - 2023)')

# xlabel indica o rótulo/legenda do eixo x
plt.xlabel('Ano')
#ylabel indica o rótulo/legenda do eixo y
plt.ylabel('PIB em USD')
# show exibe o gráfico criado.
plt.show()
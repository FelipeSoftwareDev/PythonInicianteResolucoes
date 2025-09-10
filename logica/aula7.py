# importando módulo math
import math

# sqrt é usado para descobrir a Raíz quadrada
print(math.sqrt(25))

print(math.sqrt(9))

# pow é a potência, primeiro parâmetro sendo a base e o segundo parâmetro o expoente
print(math.pow(2, 3))  # 2 elevado à 3 = 8
print(math.pow(5, 3))   # 5 elevado à 3 = 125
print(math.pow(9, 0.5))  # raiz quadrada de 9 = 3.0 


# Logaritmo em base 10
print(math.log10(100))  # 2, visto que 10² = 100

# Logaritmo em base qualquer
print(math.log(8, 2))  # 3, porque 2³ = 8 (2 vira a base)

# math.floor(): arredonda para baixo
print(math.floor(4.9))  # Saída: 4

# math.ceil(): arredonda para cima
print(math.ceil(4.1))   # Saída: 5

import random

numero = random.randint(1, 6)  # Como jogar um dado
print("Você tirou:", numero)

# Vamos sortear que jogo vamos jogar.
jogos = ["Super Mario", "Metal Slug","Golden Axe","Sonic", "The King of Fighters"]
jogo_escolhido = random.choice(jogos)
print("Vamos jogar: ",jogo_escolhido)

valor = random.random()
print(f'Número aleatório entre 0 e 1: ', valor)
print(f'Esse mesmo número com apenas 2 casas decimais: {valor:.2f}')


temperatura = random.uniform(20.0, 30.9)
print("Temperatura simulada:", temperatura)



from datetime import datetime

agora = datetime.now()
print(agora)  # exemplo: 2025-07-15 20:35:45 

print(agora.year)    # Ano
print(agora.month)   # Mês
print(agora.day)     # Dia
print(agora.hour)    # Hora
print(agora.minute)  # Minuto
print(agora.second)  # Segundo

from datetime import date 

hoje = date.today()
print(hoje)  # exemplo: 2025-07-15

nascimento = date(1999, 9, 10)
print(nascimento)

from datetime import datetime, timedelta

hoje = datetime.now()
futuro = hoje + timedelta(days=7)  # vai adicionar 7 dias
print(f"Daqui a 7 dias: {futuro}") 

prazo = datetime(2025, 12, 31)
restante = prazo - hoje
print(f"Faltam {restante.days} dias para o fim do ano!")
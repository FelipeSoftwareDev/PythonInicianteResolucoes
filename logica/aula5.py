# Listas:

bandas = ['Metallica', 'Linkin Park', 'Slipknot']

bandas.append('Sepultura')  # adiciona um item
bandas.append('Coldplay')   # adicionando outro item   
bandas.remove("Coldplay")   # remove um item
len(bandas)                 # quantidade de itens

tupla1 = ('Felipe', 25)
print(tupla1[0]) 
print(tupla1[1])

aluno = {
    "nome": "Juninho",
    "idade": 20,
    "curso": "Python",
    'nota': 10
}
print(aluno)
print(aluno['nome']) 
print(aluno["nota"])



#Operações com dict:

aluno["email"] = "juninho@email.com" # adiciona
aluno["idade"] = 26                 # atualiza

del aluno["idade"]   # remove a chave 'idade'

# iterar/percorrer o dicionário
# Chaves
for chave in aluno:
    print(chave)

# Valores
for valor in aluno.values():
    print(valor)

# Pares chave:valor
for chave, valor in aluno.items():
    print(chave, " - ", valor)

  
print(aluno)

numeros = {1, 2, 3, 3, 2}
print(numeros)  


#OPERAÇÕES:

a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)  # união → {1, 2, 3, 4, 5}
print(a & b)  # interseção → {3}


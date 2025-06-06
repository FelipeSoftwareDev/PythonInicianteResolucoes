aula = 1
while aula <= 15:
    print(f"Você já concluiu a aula {aula}!")
    aula += 1



for letra in "palavra":
    print(letra)


for animal in ("jaguatirica", "papagaio", "gorila","cachorro-caramelo"):
    print(animal)

""" 
Ex 1:

GERALMENTE chamamos de contador, ou i (de index), a variável que irá ser incrementada durante o laço
"""
contador = 0

while contador < 3:
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))

    if idade >= 18:
        print(f"{nome} é maior de idade.\n")
    else:
        print(f"{nome} é menor de idade.\n")

    contador += 1


"""
Ex 2:
No caso do exercício da tabuada, vamos inserir o laço dentro da função.
"""

def tabuada(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

num = int(input("Digite um número para ver sua tabuada: "))
tabuada(num)


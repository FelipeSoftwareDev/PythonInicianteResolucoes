#Ex 1:

def calcular_imc(peso, altura, sexo):
    imc = peso / altura**2
    if sexo == 'M' and imc <= 20 >= 25:
        print("Tudo certo")

    else:
        print("erro")

#Ex 2:

idade = int(input('Digite sua idade: '))

nome = input('Digite seu nome: ')

def verificar_maioridade(idade, nome):
    
    if idade > 18:
        print(f'Parabéns {nome} você já pode ser preso!')
    else: 
        print(f'E aí {nome} essa escola termina quando?')

verificar_maioridade(idade, nome)

#Ex 3:
habilitado = input('Voce é habilitado(a) (responder com sim ou nao): ')

def pode_dirigir(idade, nome, habilitacao):

    if idade > 18 and habilitado == "sim":
        print(f'Parabéns {nome} você já pode dirigir')

    else:
        print(f'Calma aí {nome} você ainda não atende todos requisitos para dirigir.')
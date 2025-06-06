def calcular_preco_final(preco, categoria_cliente, cupom_desconto):
    if categoria_cliente == "vip":
        desconto_cliente = preco * 0.10
    elif categoria_cliente == "funcionario":
        desconto_cliente = preco * 0.20
    else:
        desconto_cliente = 0

    # if cupom_desconto indica se ele tem cupom(cupom ==true) e o and not é para limitar o uso apenas para os clientes

    if cupom_desconto and not (categoria_cliente == "funcionario"):
        desconto_cupom = preco * 0.05
    else:
        desconto_cupom = 0

    preco_final = preco - desconto_cliente - desconto_cupom

    # Mensagem com uso do OR
    if preco_final > 100 or preco < 20:
        print(f"Sua compra totalizou R${preco_final:.2f}, você gostaria de parcelar?")
    elif preco_final <= 100 and preco_final > 0:
        print(f"Sua compra totalizou R${preco_final:.2f}")
    else:
        print("Erro: valor inválido.")

# Entrada de dados
preco_inicial = float(input("Digite o valor do produto: "))

#Receber a categoria do cliente para calcular o desconto.
categoria_cliente = input("Qual a categoria do cliente? (comum, vip, funcionario): ").lower()

# Entrada com 'sim' ou 'não' convertida para booleano

tem_cupom = input("Possui cupom de desconto? (sim/não): ").strip().lower()
cupom_desconto = tem_cupom == "sim" 
#Ou seja se a resposta for sim, cupom_desconto será verdadeiro (True)

# Chamada da função
calcular_preco_final(preco_inicial, categoria_cliente, cupom_desconto)
import sys
import os

# Garante que consiga importar os módulos vizinhos
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import acoes
import crypto

def main():
    print("Bem-vindo ao Sistema Financeiro - Aula 11")
    
    while True:
        print("\nO que você deseja analisar?")
        print("1. Ações (Stock)")
        print("2. Criptomoedas (Crypto)")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            ticker = input("Digite o ticker da Ação (ex: PETR4.SA, AAPL): ")
            acoes.analisar_acao(ticker)
        elif opcao == "2":
            ticker = input("Digite o ticker da Cripto (ex: BTC-USD, ETH-USD): ")
            crypto.analisar_crypto(ticker)
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()

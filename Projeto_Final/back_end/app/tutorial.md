# Tutorial Aula 11: Modularização e Criptomoedas

Nesta aula, vamos pegar o conhecimento da Aula 10 e dar um passo além: **Organizar nosso código**.

Imagine que seu projeto cresceu. Não dá para deixar tudo em um arquivo só (`main.py` gigante). Vamos separar as responsabilidades!

## O Objetivo
Criar um sistema que analisa tanto **Ações** quanto **Criptomoedas**, mas mantendo o código organizado em arquivos separados.

## Estrutura de Pastas
Primeiro, vamos criar uma pastinha para o nosso projeto. Dentro dela, uma pasta `app` para nosso código.

```text
Projeto_Financeiro/
│
├── app/
│   ├── acoes.py      <-- Cuida só de ações
│   ├── crypto.py     <-- Cuida só de criptomoedas (NOVO!)
│   └── main.py       <-- O chefe, que chama os outros
│
└── requirements.txt  <-- Lista do que precisamos instalar
```

## Passo 1: O arquivo de Ações (`acoes.py`)
Este arquivo será nosso "especialista" em ações.

Crie o arquivo `app/acoes.py`:

```python
import yfinance as yf

def analisar_acao(ticker):
    print(f"\n--- Analisando Ação: {ticker} ---")
    try:
        acao = yf.Ticker(ticker)
        historico = acao.history(period="1d")
        
        if not historico.empty:
            fechamento = historico['Close'].iloc[0]
            print(f"Preço: R$ {fechamento:.2f}")
        else:
            print("Dados não encontrados.")
            
    except Exception as e:
        print(f"Erro: {e}")
```

## Passo 2: O arquivo de Cripto (`crypto.py`)
Agora, o especialista em Cripto. É muito parecido, mas se precisarmos mudar algo específico para Crypto no futuro, já está separado!

Crie o arquivo `app/crypto.py`:

```python
import yfinance as yf

def analisar_crypto(ticker):
    print(f"\n--- Analisando Cripto: {ticker} ---")
    try:
        # Pega dados da cripto (Ex: BTC-USD)
        crypto = yf.Ticker(ticker)
        historico = crypto.history(period="1d")
        
        if not historico.empty:
            fechamento = historico['Close'].iloc[0]
            print(f"Preço: $ {fechamento:.2f}")
            
        info = crypto.info
        if info:
            print(f"Nome: {info.get('name', 'N/A')}")
            
    except Exception as e:
        print(f"Erro: {e}")
```

## Passo 3: O arquivo Principal (`main.py`)
Este é o arquivo que vamos executar. Ele importa os outros dois.

Crie o arquivo `app/main.py`:

```python
import acoes   # Importa nosso arquivo acoes.py
import crypto  # Importa nosso arquivo crypto.py
import sys

def main():
    while True:
        print("\n1. Ações | 2. Cripto | 0. Sair")
        opcao = input("Opção: ")
        
        if opcao == "1":
            ticker = input("Ticker (ex: PETR4.SA): ")
            acoes.analisar_acao(ticker)
        elif opcao == "2":
            ticker = input("Ticker (ex: BTC-USD): ")
            crypto.analisar_crypto(ticker)
        elif opcao == "0":
            break

if __name__ == "__main__":
    main()
```

## Como Rodar
1. Abra o terminal na pasta do projeto.
2. Instale o yfinance se ainda não tiver: `pip install yfinance`
3. Execute o main:
   ```bash
   python app/main.py
   ```

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
```

### Entendendo o "Pulo do Gato" dos Imports 🐈

Você deve ter notado estas linhas no início:
```python
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
```

**Por que isso é necessário?**
Quando o Python tenta fazer um `import`, ele procura apenas em pastas específicas. Dependendo de onde você executa o comando `python` (do terminal, do VS Code, de outra pasta), ele pode não "enxergar" os arquivos `acoes.py` e `crypto.py`, mesmo estando lado a lado.

**Passo a Passo Detalhado:**

1.  `__file__`: É uma variável mágica que contém o **caminho do arquivo atual** (o `main.py`). O problema é que as vezes esse caminho é relativo (ex: `./app/main.py`).
2.  `os.path.abspath(__file__)`: A função `abspath` (Absolute Path) converte isso para o endereço completo no seu computador (ex: `C:\Users\Voce\Projeto\app\main.py`). Isso evita confusão!
3.  `os.path.dirname(...)`: A função `dirname` (Directory Name) pega o caminho completo e "corta" o nome do arquivo final, sobrando só a pasta (ex: `C:\Users\Voce\Projeto\app`).
4.  `sys.path`: É uma lista interna do Python com todos os lugares onde ele procura imports.
5.  `.append(...)`: Adicionamos a nossa pasta `app` nessa lista!

**Resultado:** O Python agora sabe exatamente onde procurar os arquivos vizinhos, não importa de onde você rodou o programa.

## Como Rodar
1. Abra o terminal na pasta do projeto.
2. Instale o yfinance se ainda não tiver: `pip install yfinance`
3. Execute o main:
   ```bash
   python app/main.py
   ```

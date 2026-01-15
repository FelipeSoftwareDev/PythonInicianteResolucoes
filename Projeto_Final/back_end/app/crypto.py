import yfinance as yf

def analisar_crypto(ticker):
    """
    Função simples para analisar criptomoedas.
    Recebe o ticker de uma cripto (ex: BTC-USD) e imprime informações.
    """
    print(f"\n--- Analisando Cripto: {ticker} ---")
    
    try:
        # O yfinance trata cripto de forma muito parecida com ações
        crypto = yf.Ticker(ticker)
        
        # Pegando o histórico recente
        historico = crypto.history(period="1d")
        
        if not historico.empty:
            # Observação: Criptos geralmente são cotadas em outra moeda (USD, BRL)
            fechamento = historico['Close'].iloc[0]
            print(f"Preço atual (aprox.): {fechamento:.2f}")
        else:
            print("Dados não encontrados.")
            
        # Traz informações extras se disponíveis
        info = crypto.info
        if info:
            print(f"Nome: {info.get('name', 'N/A')}")
            print(f"Market Cap: {info.get('marketCap', 'N/A')}")
            
    except Exception as e:
        print(f"Erro ao analisar a cripto {ticker}: {e}")

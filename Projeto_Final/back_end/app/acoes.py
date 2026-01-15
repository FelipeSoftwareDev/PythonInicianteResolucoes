import yfinance as yf

def analisar_acao(ticker):
    """
    Função simples para analisar ações.
    Recebe o ticker de uma ação (ex: PETR4.SA) e imprime informações.
    """
    print(f"\n--- Analisando Ação: {ticker} ---")
    
    try:
        # Criando o objeto Ticker
        acao = yf.Ticker(ticker)
        
        # Pegando o histórico recente (último dia) para ver o preço atual
        historico = acao.history(period="1d")
        
        if not historico.empty:
            fechamento = historico['Close'].iloc[0]
            print(f"Preço de fechamento mais recente: R$ {fechamento:.2f}")
        else:
            print("Dados históricos não encontrados.")
            
        # Pega informações básicas se disponíveis
        info = acao.info
        if info:
            print(f"Setor: {info.get('sector', 'N/A')}")
            print(f"Empresa: {info.get('longName', 'N/A')}")
            
    except Exception as e:
        print(f"Erro ao analisar a ação {ticker}: {e}")

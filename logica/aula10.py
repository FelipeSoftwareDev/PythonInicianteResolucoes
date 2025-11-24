import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# --- Entrada de dados ---
ativo1 = input("Digite o primeiro ativo (ex: AAPL): ").upper()
ativo2 = input("Digite o segundo ativo (ex: MSFT): ").upper()

# --- Download dos dados ---
dados1 = yf.download(ativo1, period="6mo")
dados2 = yf.download(ativo2, period="6mo")

# --- Cálculo da SMA20 ---
dados1["SMA20"] = dados1["Close"].rolling(window=20).mean()
dados2["SMA20"] = dados2["Close"].rolling(window=20).mean()


# --- Tamanho do gráfico ---
plt.figure(figsize=(12,6))

# --- Ativo 1 ---
# Valor de fechamento
plt.plot(dados1.index, dados1["Close"], 
         label=f"{ativo1} Fechamento", 
         color="dodgerblue", linewidth=2)
# SMA20
plt.plot(dados1.index, dados1["SMA20"], 
         label=f"{ativo1} SMA20", 
         color="#00ffea", linestyle="--", linewidth=2)

# --- Ativo 2 ---
plt.plot(dados2.index, dados2["Close"], 
         label=f"{ativo2} Fechamento", 
         color="orangered", linewidth=2)

plt.plot(dados2.index, dados2["SMA20"], 
         label=f"{ativo2} SMA20", 
         color="#FF2121", linestyle="--", linewidth=2)

# --- Personalização ---
plt.title(f"Comparação entre {ativo1} e {ativo2} - Preço + SMA20", fontsize=14, fontweight="bold")
plt.xlabel("Data", fontsize=12)
plt.ylabel("Preço de Fechamento (USD)", fontsize=12)
plt.legend(loc="upper left", bbox_to_anchor=(1,1))  # legenda fora do gráfico
plt.grid(alpha=0.3) # grade em linhas semi transparentes
plt.gca().set_facecolor("#444444") # cor de fundo do gráfico

plt.tight_layout()
plt.show()
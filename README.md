# Impacto da Volatilidade das Criptomoedas no Interesse dos Investidores

Este projeto tem como objetivo analisar a relação entre a volatilidade do mercado de criptomoedas e o interesse dos investidores, utilizando como base o preço do Bitcoin e o volume de buscas no Google Trends.

---

##  1. Problema

A alta volatilidade das criptomoedas é um fator que influencia diretamente o comportamento dos investidores, tanto experientes quanto iniciantes. Neste projeto, buscamos compreender se há uma correlação entre os picos de volatilidade do Bitcoin e o aumento de interesse (medido por volume de buscas no Google).

---

##  2. Fontes de Dados

- **CoinGecko API**  
  Dados históricos de preços do Bitcoin, coletados por meio da API pública.

- **Google Trends**  
  Volume de buscas pela palavra-chave “Bitcoin”, coletado via interface web e exportado em CSV.

---

##  3. Estrutura do Projeto


---

##  4. Análise e Visualização

Foi realizada uma análise exploratória com Python e visualizações no Looker Studio.

###  Principais Insights:
- O aumento no volume de buscas ocorre frequentemente após oscilações acentuadas no preço do Bitcoin.
- Há forte correlação entre alta volatilidade e maior interesse de busca.
- Investidores parecem reagir mais a perdas ou ganhos extremos do que a períodos estáveis.

###  Visualização (Exemplo):

![Gráfico de tendência](visuals/visuals_bitcoin_trends.png)

> Gráfico mostrando a comparação entre o preço do Bitcoin e o interesse no Google Trends.

---

##  5. Conclusão

A análise sugere que a percepção de risco influencia diretamente o interesse dos investidores em criptomoedas. Com base nesses dados, é possível prever comportamentos de busca e engajamento do público com base nas movimentações do mercado.

---

##  Próximos passos

- Ampliar o estudo para outras criptomoedas além do Bitcoin
- Incorporar dados sociais (Twitter, Reddit)
- Incluir análises de sentimento e volume de transações

---

##  Feito com:

- Python (pandas, matplotlib)
- Google Trends
- CoinGecko API
- Looker Studio


## instruções de uso no README
- python scripts/coleta_preco_cripto.py
- python scripts/coleta_google_trends.py
- python scripts/trata_dados.py

# /scripts/trata_dados.py
import pandas as pd

def merge_dados():
    preco = pd.read_csv("data/raw/bitcoin_price_historical.csv", parse_dates=["date"])
    trends = pd.read_csv("data/raw/google_trends_bitcoin.csv", parse_dates=["date"])

    df = pd.merge(preco, trends, on="date", how="inner")
    df.rename(columns={"Bitcoin": "google_trends_score"}, inplace=True)
    df.to_csv("data/processed/dados_tratados.csv", index=False)
    print("✅ Dados tratados salvos com sucesso!")

if __name__ == "__main__":
    merge_dados()

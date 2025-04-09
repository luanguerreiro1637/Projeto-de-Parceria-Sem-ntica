# /scripts/coleta_preco_cripto.py
import pandas as pd
import requests
from datetime import datetime

def fetch_bitcoin_price_history():
    url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
    params = {
        "vs_currency": "usd",
        "days": "max",
        "interval": "daily"
    }
    response = requests.get(url, params=params)
    data = response.json()

    prices = data["prices"]
    df = pd.DataFrame(prices, columns=["timestamp", "price"])
    df["date"] = pd.to_datetime(df["timestamp"], unit="ms")
    df = df[["date", "price"]]
    df.to_csv("data/raw/bitcoin_price_historical.csv", index=False)
    print("✅ Dados de preço salvos com sucesso!")

if __name__ == "__main__":
    fetch_bitcoin_price_history()

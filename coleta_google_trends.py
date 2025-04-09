# /scripts/coleta_google_trends.py
from pytrends.request import TrendReq
import pandas as pd

def fetch_google_trends(keyword="Bitcoin"):
    pytrends = TrendReq(hl='en-US', tz=0)
    pytrends.build_payload([keyword], timeframe='today 5-y')
    data = pytrends.interest_over_time()
    if "isPartial" in data.columns:
        data = data.drop(columns=["isPartial"])
    data.reset_index(inplace=True)
    data.to_csv("data/raw/google_trends_bitcoin.csv", index=False)
    print("✅ Dados do Google Trends salvos com sucesso!")

if __name__ == "__main__":
    fetch_google_trends()

import requests
import schedule
import time
from telegram import Bot

TOKEN = '' #Botun token bilgisini girin
CHAT_ID = '' #Botun mesaj atacağı chat in ID sini girin

bot = Bot(token=TOKEN)

def get_prices():
    url = 'https://api.coingecko.com/api/v3/simple/price'
    params = {
        "ids": "bitcoin,ethereum,solana,binancecoin,ripple,avalanche-2", 
        "vs_currencies": "usd"
    }
    response = requests.get(url, params=params)
    data = response.json()

    btc = data["bitcoin"]["usd"]
    eth = data["ethereum"]["usd"]
    sol = data["solana"]["usd"]
    bnb = data["binancecoin"]["usd"]
    xrp = data["ripple"]["usd"]  
    avax = data["avalanche-2"]["usd"]

    message = f"---Anlık Kripto Fiyatları---\n\n" \
              f"🟡 Bitcoin (BTC): ${btc}\n" \
              f"🔵 Ethereum (ETH): ${eth}\n" \
              f"🟢 Solana (SOL): ${sol}\n" \
              f"🟡 Binance Coin (BNB): ${bnb}\n" \
              f"⚫️ XRP (XRP): ${xrp}\n" \
              f"🔴 Avalanche (AVAX): ${avax}"

    telegram_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    requests.post(telegram_url, data=payload)
schedule.every().day.at("09:00").do(get_prices)
schedule.every().day.at("21:00").do(get_prices)

while True:
    schedule.run_pending()
    time.sleep(60)

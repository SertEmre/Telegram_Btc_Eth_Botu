import requests
import schedule
import time
import os
from dotenv import load_dotenv
from telegram import Bot

load_dotenv()

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

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

    bot.send_message(chat_id=CHAT_ID, text=message)
schedule.every().day.at("09:00").do(get_prices)
schedule.every().day.at("21:00").do(get_prices)

while True:
    schedule.run_pending()
    time.sleep(60)

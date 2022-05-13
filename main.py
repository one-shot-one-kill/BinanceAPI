import requests


url = "https://api.binance.com/api/v3/ticker/price?symbol={}USDT"

btc = "BTC"

res = requests.get(url.format(btc)).json()

print(res['price'])
import requests
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render

from .forms import CoinForm
from .models import CoinName


def index(request):
    url = "https://api.binance.com/api/v3/ticker/price?symbol={}USDT"

    if request.method == "POST":
        form = CoinForm(request.POST)
        form.save()

    form = CoinForm()

    coins = CoinName.objects.all()[:5]

    all_coins = []

    for coin in coins:
        res = requests.get(url.format(coin)).json()

        coin_info = {
            'symb': res['symbol'],
            'price': res['price'],
            'id': coin.id
        }

        all_coins.append(coin_info)

    context = {'all_coins': all_coins, 'form': form}

    return render(request, 'index.html', context)


def delete(request, id):
    try:
        coins = CoinName.objects.get(id=id)
        coins.delete()
        return HttpResponseRedirect("/")
    except CoinName.DoesNotExist:
        return HttpResponseNotFound("<h2>Coin not found</h2>")
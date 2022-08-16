from pycoingecko import CoinGeckoAPI
import json

with open("Portfolio.json") as f:
    portfolio = json.load(f)

cg = CoinGeckoAPI()

nameIndex = {}
ticker = cg.get_coins_list()


def findInfo(id):
    list = cg.get_price(
        ids=id,
        vs_currencies="usd",
        include_market_cap="true",
        include_24hr_vol="true",
        include_24hr_change="true",
        include_last_updated_at="false",
    )
    return list[id]


data = []
for coin in portfolio["portfolio"]:
    coinInfo = findInfo(coin["name"].lower())
    id = coin["id"]
    spentAmmount = int(1000*(float(coin["price"]) * float(coin["ammount"])))/1000
    currentWorth = int(1000*(float(coinInfo["usd"]) * float(coin["ammount"])))/1000
    roi = int((1000*(float(coinInfo["usd"]) - float(coin["price"])) * 100 / (float(coin["price"]))))/1000
    difference = int((1000*(currentWorth - spentAmmount)))/1000

    data.append(
        [str(id), str(spentAmmount), str(currentWorth), str(roi), str(difference)]
    )
    print("ID, SPENT AMOUNT,CURRENT WORTH, ROI, DIFF")
    print([str(id), str(spentAmmount), str(currentWorth), str(roi), str(difference)])


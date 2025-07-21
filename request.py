import requests

urlEndPoint = "https://steamcommunity.com/market/priceoverview/?"
currency = "currency=2&"
appid = "appid=730&"
marketHash = "market_hash_name="

#url = "https://steamcommunity.com/market/priceoverview/?appid=730&currency=23&market_hash_name=Fracture%20Case"
#response = requests.get(url)
#print(response.json())

marketHashDictionary = {
    "snakebiteCase": "Snakebite%20Case",
    "fractureCase": "Fracture%20Case",
    "stockholm2021ContendersStickerCapsule": "Stockholm%202021%20Contenders%20Sticker%20Capsule",
    "spectrum2Case": "Spectrum%202%20Case",
    "recoilCase": "Recoil%20Case",
    "clutchCase": "Clutch%20Case",
}

def ItemRequest(itemName) -> list:
    url = urlEndPoint + appid + currency + marketHash + marketHashDictionary[itemName]
    print(url)
    response = requests.get(url)
    data = response.json()

    lowestPrice = float(data.get("lowest_price")[1:])  # Assumes £ sign
    volume = int(data.get("volume").replace(',', ''))
    medianPrice = float(data.get("median_price")[1:])

    return [lowestPrice, medianPrice, volume]
    
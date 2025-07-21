from request import ItemRequest

itemsList = ["snakebiteCase", "fractureCase", "stockholm2021ContendersStickerCapsule", "spectrum2Case", "recoilCase"]

itemsDict = {}


for item in itemsList:
    itemsDict[item] = ItemRequest(item)

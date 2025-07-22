from data_processor import GetTodaysData
from telegram import SendMessage, CreateMessage
#itemsList = ["snakebiteCase", "fractureCase", "stockholm2021ContendersStickerCapsule", "spectrum2Case", "recoilCase"]
inventoryDict = {
    #"ItemName": [price, quantity]
    "snakebiteCase": [0.10, 500],
    "fractureCase": [0.17, 1000],
}

CreateMessage(GetTodaysData(inventoryDict), inventoryDict)

SendMessage()

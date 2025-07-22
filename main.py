from data_processor import GetTodaysData
from dotenv import load_dotenv
import os

load_dotenv()

botToken = os.getenv("BOT_TOKEN")
chatID = os.getenv("CHAT_ID")
print(chatID)
#itemsList = ["snakebiteCase", "fractureCase", "stockholm2021ContendersStickerCapsule", "spectrum2Case", "recoilCase"]
inventoryDict = {
    #"ItemName": [price, quantity]
    "snakebiteCase": [0.10, 500],
    "fractureCase": [0.17, 1000],
}

print(GetTodaysData(inventoryDict))

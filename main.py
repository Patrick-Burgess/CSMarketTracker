import sys
from data_processor import GetTodaysData
from telegram import SendMessage, CreateMessage
from historicaldata import depositdata
# Trivial comment    

inventoryDict = {
    #"ItemName": [price, quantity]
    "snakebiteCase": [0.10, 500],
    "fractureCase": [0.17, 1000],
    "spectrum2Case":[1.11, 79],
    "recoilCase":[0.09, 1373],
    "clutchCase":[0.30, 500],
    "austin2025ChallengersAutographCapsule": [0.24,80],
    "austin2025LegendsStickerCapsule": [0.21,300],
    "stockholm2021ContendersStickerCapsule": [1.74,15]
}
todaysData = GetTodaysData(inventoryDict)

#Store Data code
#depositdata(todaysData)

if todaysData == None:
    print("Error: Failed to retrieve today's data. Exiting...")
    sys.exit()


SendMessage(CreateMessage(todaysData, inventoryDict))
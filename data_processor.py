from request import ItemRequest
def GetTodaysData(inventoryDict):
    itemsDict = {}

    for item in inventoryDict:
        itemsDict[item] = ItemRequest(item)
    todaysData = {
        #"CaseName": [Total Value, ProfitnLoss, PNL Percentage]
    }

    for item in inventoryDict:
        todaysData[item] = [None,None,None]
        #Total Value
        todaysData[item][0] = inventoryDict[item][1]*itemsDict[item][1]
        initialInvestValue = inventoryDict[item][0]*inventoryDict[item][1]
        #PNL
        todaysData[item][1] =  todaysData[item][0] - initialInvestValue
        #PNL%
        todaysData[item][2] = (todaysData[item][0] - initialInvestValue)/initialInvestValue*100

    return todaysData
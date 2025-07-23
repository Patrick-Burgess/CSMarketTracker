from request import ItemRequest
def GetTodaysData(inventoryDict):
    errorFlag = False
    itemsDict = {}

    for item in inventoryDict:
        result = ItemRequest(item)
        if result is None:
            errorFlag = True
            print(f"Error: Failed to fetch data for {item}. Skipping...")
            continue  # Skip this item if the request failed
        itemsDict[item] = result
    
    todaysData = {
        #"CaseName": [Total Value, ProfitnLoss, PNL Percentage]
    }
    if errorFlag:
        return None
    
    for item in inventoryDict:
        todaysData[item] = [None,None,None,None]
        #Current price
        todaysData[item][0] = itemsDict[item][1]
        #Total Value
        todaysData[item][1] = inventoryDict[item][1]*itemsDict[item][1]
        initialInvestValue = inventoryDict[item][0]*inventoryDict[item][1]
        #PNL
        todaysData[item][2] =  todaysData[item][1] - initialInvestValue
        #PNL%
        todaysData[item][3] = (todaysData[item][1] - initialInvestValue)/initialInvestValue*100

    return todaysData
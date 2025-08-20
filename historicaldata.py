import json
from datetime import date
def depositdata(todaysData):
    jsonentry = {
        str(date.today()): {
            item: {
                "price": values[0],  # Extract price from the list
                "volume": values[4]  # Extract volume from the list
            }
            for item, values in todaysData.items()
        }
    }
    try:
        with open("historical_data.json", "r") as file:
            historicaldatajson = json.load(file)
    except FileNotFoundError:
        historicaldatajson = {}
    historicaldatajson.update(jsonentry)
    with open("historical_data.json", "w") as file:
        json.dump(historicaldatajson, file, indent=4)

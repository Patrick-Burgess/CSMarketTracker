from dotenv import load_dotenv
import os
import requests






def CreateMessage(todaysData, portfolio):
    print(todaysData,portfolio)
    message = ""

    totalPortfolioValue = sum(todaysData[item][1] for item in portfolio)
    message += (
        f"📊 *Portfolio Update*\n"
        f"💰 Total Portfolio Value: £{totalPortfolioValue:.2f}\n"
        f"------------------------------\n"

    )

    for item in portfolio:
        itemMessage = (
            f"📦 *{item.replace('Case', ' Case')}*\n"
            f"🔹 Bought: {portfolio[item][1]} at £{portfolio[item][0]:.2f}\n"
            f"💸 Total Invested: £{portfolio[item][1] * portfolio[item][0]:.2f}\n"
            f"💰 Current Price: £{todaysData[item][0]:.2f}\n"
            f"📊 Total Value: £{todaysData[item][1]:.2f}\n"
            f"📈 PNL: £{todaysData[item][2]:.2f} ({todaysData[item][3]:.2f}%)\n"
            f"------------------------------\n"
        )
        message += itemMessage
    return message
     

def SendMessage(message):
    load_dotenv()
    botToken = os.getenv("BOT_TOKEN")
    chatID = os.getenv("CHAT_ID")
    if not botToken or not chatID:
        raise ValueError("Missing required environment variables.")

    url = f'https://api.telegram.org/bot{botToken}/sendMessage'

    payload = {
        'chat_id': chatID,
        'text': message
    }

    response = requests.post(url, data=payload)
    return response

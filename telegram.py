from dotenv import load_dotenv
import os
import requests

def CreateMessage(todaysData, portfolio):
    for item in portfolio:
        message = message = f"""📦 {item}
• Buy Price: ${buy_price}
• Quantity: {quantity}
• Current Price: ${curr_price}
"""
     


def SendMessage(message):
    load_dotenv()
    botToken = os.getenv("BOT_TOKEN")
    chatID = os.getenv("CHAT_ID")
    url = f'https://api.telegram.org/bot{botToken}/sendMessage'

    payload = {
        'chat_id': chatID,
        'text': message
    }

    response = requests.post(url, data=payload)
    return response

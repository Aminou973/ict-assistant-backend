import requests
from discord_config import WEBHOOK_URL
from responses import get_start_day_message

def send_start_day_message():
    data = {
        "content": get_start_day_message()
    }
    response = requests.post(WEBHOOK_URL, json=data)
    return response.status_code
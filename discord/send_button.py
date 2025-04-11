import requests
from discord_config import WEBHOOK_URL

button_message = {
    "content": "**Assistant IA Ready** 🚀\nClique sur le bouton pour démarrer la journée :",
    "components": [
        {
            "type": 1,
            "components": [
                {
                    "type": 2,
                    "style": 1,
                    "label": "📋 Démarrer la Journée",
                    "custom_id": "start_day_button"
                }
            ]
        }
    ]
}

response = requests.post(WEBHOOK_URL, json=button_message)
print("Status:", response.status_code)
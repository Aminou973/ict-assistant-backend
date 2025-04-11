from datetime import datetime

def get_daily_calendar_message():
    now = datetime.now()
    today = now.strftime("%A %d %B %Y")
    return f"""📆 **Calendrier du jour – {today}**

✅ Merci de confirmer ta disponibilité pour trader aujourd’hui.

🕒 Sessions :
- London : 03:00 - 05:00 NY
- NY AM : 08:30 - 11:00 NY
- NY PM : 13:00 - 16:00 NY

📌 **Rappel IA** :
- As-tu bien consulté les news macro ?
- Est-ce un jour à éviter selon ton plan ? (ex: CPI, NFP, FOMC...)

🧠 Clique sur le bouton ci-dessous pour signaler ta présence.
"""
from fastapi import APIRouter
from discord_ui import send_start_day_message

router = APIRouter()

@router.post("/trigger/start-day")
def trigger_start_day():
    return {"status": send_start_day_message()}

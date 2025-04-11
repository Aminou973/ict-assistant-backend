from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def start_day():
    return {"message": "Start of the trading day initialized"}
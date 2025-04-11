from fastapi import APIRouter

router = APIRouter()

@router.post("/")
def log_trade():
    return {"message": "Trade has been logged successfully"}
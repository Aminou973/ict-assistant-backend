from fastapi import APIRouter

router = APIRouter()

@router.post("/")
def rex_daily():
    return {"message": "Daily REX has been recorded"}
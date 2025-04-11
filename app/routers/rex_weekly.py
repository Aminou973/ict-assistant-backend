from fastapi import APIRouter

router = APIRouter()

@router.post("/")
def rex_weekly():
    return {"message": "Weekly REX has been recorded"}
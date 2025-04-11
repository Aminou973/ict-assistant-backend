from fastapi import FastAPI
from app.routers import start_day, log_trade, rex_daily, rex_weekly
# Optionnel : importer goals uniquement si utilisé
# from app.routers import goals

app = FastAPI()

@app.get("/")
def root():
    return {"status": "Assistant IA Discord is running 👨‍💻"}

# ROUTES ACTIVES
app.include_router(start_day.router, prefix="/start-day")
app.include_router(log_trade.router, prefix="/log-trade")
app.include_router(rex_daily.router, prefix="/rex-daily")
app.include_router(rex_weekly.router, prefix="/rex-weekly")

# Optionnel :
# app.include_router(goals.router, prefix="/goals", tags=["Goals"])

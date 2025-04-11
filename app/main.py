from fastapi import FastAPI
from app.routers import start_day, log_trade, rex_daily, rex_weekly

app = FastAPI()


app.include_router(goals.router, prefix="/goals", tags=["Goals"])
app.include_router(rex.router, prefix="/rex", tags=["REX"])
app.include_router(setup.router, prefix="/setup", tags=["Setup"])
app.include_router(discord.router, tags=["Discord"])

@app.get("/")
def read_root():
    return {"message": "Assistant IA Backend V2 Ready"}

# Routes IA interactives
app.include_router(start_day.router, prefix="/start-day")
app.include_router(log_trade.router, prefix="/log-trade")
app.include_router(rex_daily.router, prefix="/rex-daily")
app.include_router(rex_weekly.router, prefix="/rex-weekly")

@app.get("/")
def root():
    return {"status": "Assistant IA Discord is running 👨‍💻"}

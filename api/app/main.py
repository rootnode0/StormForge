from fastapi import FastAPI
from app.worker import run_mission
import uuid
from app.chaos import set_chaos_state, get_chaos_state

app = FastAPI()

@app.get("/")
def root():
    return {"message": "StormForge running"}

@app.post("/chaos/start")
def start_chaos():
    set_chaos_state(True)
    return {"status": "chaos started"}

@app.post("/chaos/stop")
def stop_chaos():
    set_chaos_state(False)
    return {"status": "chaos stopped"}

@app.get("/chaos/status")
def chaos_status():
    return {"enabled": get_chaos_state()}

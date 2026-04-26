from fastapi import FastAPI
from app.worker import run_mission
import uuid

app = FastAPI()

@app.get("/")
def root():
    return {"message": "StormForge running"}

@app.post("/mission/start")
def start_mission():
    mission_id = str(uuid.uuid4())
    run_mission.delay(mission_id)
    return {"mission_id": mission_id}

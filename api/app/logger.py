import os
from datetime import datetime

LOG_DIR = "/app/logs"

def log_message(mission_id, message):
    os.makedirs(LOG_DIR, exist_ok=True)
    file_path = f"{LOG_DIR}/{mission_id}.log"

    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, "a") as f:
        f.write(f"[{timestamp}] {message}\n")

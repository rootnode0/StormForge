import os

LOG_DIR = "/app/logs"

def log_message(mission_id, message):
    os.makedirs(LOG_DIR, exist_ok=True)
    file_path = f"{LOG_DIR}/{mission_id}.log"

    with open(file_path, "a") as f:
        f.write(message + "\n")

import random
import time
import requests

def chaos_task(mission_id):
    delay = random.uniform(0.5, 3)
    time.sleep(delay)

    if random.random() < 0.3:
        raise Exception("🔥 Chaos failure occurred")

    # external call
    requests.get("https://httpbin.org/delay/1")

    return f"Mission {mission_id} completed"

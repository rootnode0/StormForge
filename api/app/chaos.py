import random
import time
import requests

CHAOS_ENABLED = True

def chaos_task(mission_id):
    if not CHAOS_ENABLED:
        return f"Mission {mission_id} skipped (chaos stopped)"
    delay = random.uniform(0.5, 3)
    time.sleep(delay)

    if random.random() < 0.3:
        raise Exception("🔥 Chaos failure occurred")

    # external call
    requests.get("https://httpbin.org/delay/1")

    return f"Mission {mission_id} completed"

def set_chaos_state(state: bool):
    global CHAOS_ENABLED
    CHAOS_ENABLED = state

def get_chaos_state():
    return CHAOS_ENABLED

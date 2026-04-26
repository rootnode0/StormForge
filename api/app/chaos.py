import random
import time
import requests
import redis

# Redis for shared state
r = redis.Redis(host="redis", port=6379, db=1)

def set_chaos_state(state: bool):
    r.set("chaos_enabled", int(state))

def get_chaos_state():
    val = r.get("chaos_enabled")
    return bool(int(val)) if val else True


# 🔥 THIS WAS MISSING / BROKEN
def chaos_task(mission_id):
    delay = random.uniform(0.5, 3)
    time.sleep(delay)

    if random.random() < 0.3:
        raise Exception("🔥 Chaos failure occurred")

    # external call
    requests.get("https://httpbin.org/delay/1")

    return f"Mission {mission_id} completed"

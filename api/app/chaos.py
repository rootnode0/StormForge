import redis

r = redis.Redis(host="redis", port=6379, db=1)

def set_chaos_state(state: bool):
    r.set("chaos_enabled", int(state))

def get_chaos_state():
    val = r.get("chaos_enabled")
    return bool(int(val)) if val else True

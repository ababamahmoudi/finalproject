import os
import redis
import json

REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379/0")

redis_client = redis.Redis.from_url(REDIS_URL, decode_responses=True)

def get_cached_json(key: str):
    data = redis_client.get(key)
    if data:
        return json.loads(data)
    return None

def set_cached_json(key: str, value, ttl_seconds: int = 60):
    redis_client.set(key, json.dumps(value), ex=ttl_seconds)

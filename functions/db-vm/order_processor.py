import redis
import json
import time

r = redis.Redis(host='10.2.113.134', port=6379, db=0, decode_responses=True)

print("order_processor started...")

while True:
    order_json = r.lpop("orders")
    if order_json:
        order = json.loads(order_json)
        print(f"Processing order: {order}")
        # simulate work
        time.sleep(2)
        print("Order processed.")
    time.sleep(1)

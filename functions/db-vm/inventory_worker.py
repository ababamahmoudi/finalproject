import redis
import json
import time

r = redis.Redis(host='10.2.113.134', port=6379, db=0, decode_responses=True)

print("inventory_worker started...")

while True:
    event = r.lpop("inventory")
    if event:
        data = json.loads(event)
        print(f"Updating inventory for product {data['product_id']} quantity {data['quantity']}")
        time.sleep(1)
        print("> Inventory updated.")
    time.sleep(1)

import redis
import json
import time

r = redis.Redis(host='10.2.113.134', port=6379, db=0, decode_responses=True)

print("email_notifier started...")

while True:
    msg = r.lpop("emails")
    if msg:
        data = json.loads(msg)
        print(f"Sending email to {data['email']}: {data['message']}")
        time.sleep(1)
        print("> Email sent.")
    time.sleep(1)

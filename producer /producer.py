from kafka import KafkaProducer
import json
import time
import uuid
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

topic = "orders"

while True:
    order = {
        "order_id": str(uuid.uuid4()),
        "customer_id": random.randint(1000, 9999),
        "amount": round(random.uniform(100, 5000), 2),
        "status": "CREATED"
    }
    producer.send(topic, order)
    producer.flush()
    print("Produced:", order)
    time.sleep(3)

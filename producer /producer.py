from kafka import KafkaProducer
import json
import time
import uuid
import random
import logging

logging.basicConfig(level=logging.INFO)

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    retries=5,
    acks='all'
)

while True:
    order = {
        "order_id": str(uuid.uuid4()),
        "customer_id": random.randint(1000, 9999),
        "amount": round(random.uniform(100, 5000), 2),
        "status": "CREATED"
    }

    producer.send("orders", order)
    logging.info(f"Produced: {order}")
    time.sleep(2)

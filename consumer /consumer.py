from kafka import KafkaConsumer
import json
import logging
import time

logging.basicConfig(level=logging.INFO)

consumer = KafkaConsumer(
    "orders",
    bootstrap_servers='kafka:9092',
    group_id="order-processing-group",
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

for message in consumer:
    order = message.value
    logging.info(f"Received order: {order}")

    # Simulate processing
    time.sleep(1)
    logging.info(f"Order {order['order_id']} processed successfully.")

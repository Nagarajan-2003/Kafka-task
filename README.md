# Kafka Order Processing Project

## Description

This project demonstrates a real-time event streaming system using Apache Kafka.

A Producer application sends order messages to Kafka.

A Consumer application receives those messages from Kafka.

Kafka acts as a message broker between the producer and consumer.

This architecture simulates real-world order processing systems.

## Project Structure

kafka-production

docker-compose.yml → Kafka & Zookeeper configuration
producer/producer.py → Producer application
consumer/consumer.py → Consumer application
README.md → Documentation

## Technologies Used

Docker
Docker Compose
Apache Kafka
Apache Zookeeper
Python
kafka-python



## Installation Steps

1. Install Docker Desktop

2. Disable Kubernetes in Docker Desktop settings

3. Install Python

4. Install required Python dependency

pip install kafka-python



## Running the Project

Start Kafka and Zookeeper:

docker compose up -d

Verify containers are running:

docker ps

Output:

zookeeper   Up
kafka       Up



Start Consumer (Terminal 1):

python consumer/consumer.py



Start Producer (Terminal 2):

python producer/producer.py



## Testing

When Producer runs, it generates order messages.

Producer Output:

Produced: {order_id, customer_id, amount, status}

Consumer Output:

Consumed: {order_id, customer_id, amount, status}

This confirms the end-to-end message flow is working.


## How Kafka Works in This Project

Producer → Kafka Broker → Consumer

The producer sends order data to a Kafka topic.

Kafka stores the message.

The consumer reads the message from the topic.


## Features

Real-time message streaming
Producer–Consumer architecture
Docker-based Kafka setup
JSON message serialization
Order event simulation



## Conclusion

This project demonstrates a working Apache Kafka setup using Docker and Python.

It shows how real-time event streaming works using producer and consumer architecture.

This setup can be extended for microservices, event-driven systems, and real-time data processing applications.

from kafka import KafkaProducer
import json

# Налаштування Kafka Producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    key_serializer=lambda v: v,  #  вже передаю закодовані в байти key та value
    value_serializer=lambda v: v
)

def send_to_kafka(topic, key, value):
    producer.send(topic, key=key, value=value)
    print(f"Sent to Kafka | Key: {key} | Value: {value}")

# Закриття продюсера при завершенні
def close_producer():
    producer.flush()
    producer.close()

from kafka import KafkaProducer
import json

# Ініціалізація Kafka Producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    key_serializer=lambda v: json.dumps(v).encode('utf-8') if isinstance(v, dict) else v,
    value_serializer=lambda v: json.dumps(v).encode('utf-8') if isinstance(v, dict) else v
)

# Функція для надсилання повідомлення у Kafka
def send_to_kafka(topic, key, value):
    producer.send(topic, key=key, value=value)
    print(f"Sent to Kafka | Key: {key} | Value: {value}")

# Закриття продюсера при завершенні
def close_producer():
    producer.flush()
    producer.close()
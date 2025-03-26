import os
import json
from kafka import KafkaConsumer

ALLOWED_EVENT_TYPES = os.getenv("ENABLED_EVENT_TYPES", "Click,Login,Search,Comment").split(",")

consumer = KafkaConsumer(
    "user_events",
    bootstrap_servers="localhost:9092",
    group_id="user-events-group",
    value_deserializer=lambda v: json.loads(v.decode("utf-8"))
)

for message in consumer:
    event = message.value
    if event.get("event_type") in ALLOWED_EVENT_TYPES:
        print(f"Received allowed event: {event}")
    else:
        print(f"Filtered out event: {event.get('event_type')}")

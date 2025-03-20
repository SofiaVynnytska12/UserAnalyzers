import random
import uuid
import json
from datetime import datetime

# Функція для генерації випадкових даних для різних типів подій
def generate_data():
    event_type = random.choice(["Login", "Click", "Search", "Comment"])
    timestamp = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')

    if event_type == "Login":
        return {
            "event_type": event_type,
            "user_id": str(uuid.uuid4()),
            "username": f"user_{random.randint(1, 1000)}",
            "email": f"user{random.randint(1, 1000)}@example.com",
            "country": random.choice(["US", "UA", "PL", "GB", "DE"]),
            "timestamp": timestamp
        }
    elif event_type == "Click":
        return {
            "event_type": event_type,
            "user_id": str(uuid.uuid4()),
            "element_id": f"button_{random.randint(1, 100)}",
            "page_url": f"https://example.com/page{random.randint(1, 10)}",
            "timestamp": timestamp
        }
    elif event_type == "Search":
        return {
            "event_type": event_type,
            "user_id": str(uuid.uuid4()),
            "search_query": random.choice(["data analysis", "machine learning", "big data", "cloud computing", "AI trends"]),
            "timestamp": timestamp
        }
    elif event_type == "Comment":
        return {
            "event_type": event_type,
            "user_id": str(uuid.uuid4()),
            "username": f"user_{random.randint(1, 1000)}",
            "comment_text": random.choice(["Great post!", "I disagree", "Nice article!", "Thanks for sharing"]),
            "post_id": str(uuid.uuid4()),
            "timestamp": timestamp
        }

# Функція для перетворення даних у JSON
def generate_json_data():
    data = generate_data()
    key = {
        "timestamp": data["timestamp"],
        "uuid": str(uuid.uuid4()),
        "service_name": "UserAnalyzer",
        "event_type": data["event_type"]
    }
    return json.dumps(key).encode('utf-8'), json.dumps(data).encode('utf-8')
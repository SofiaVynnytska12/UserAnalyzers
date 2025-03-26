# UserAnalyzers

### Implement Data Generation and Publishing into Kafka

This component is responsible for generating mock user activity data and sending it to a Kafka topic named `user_events`. It simulates events like clicks, logins, searches, and comments for later processing by the consumer.

---

#### Project Structure

```
kafka_producer/
├── data_generator.py     # Generates random user activity events
├── kafka_producer.py     # Sends events to Kafka
└── scheduler.py          # Schedules sending events every 10 seconds
```

---

#### Functionality

- **Key generation:**  
  Each message sent to Kafka has a key that includes:
  - Timestamp (`ISO 8601`)
  - UUID
  - Service name (`UserAnalyzer`)
  - Event type

- **Value generation:**  
  Data is randomly generated according to a mock schema (click, login, search, comment).

- **Kafka integration:**  
  Messages are sent to the topic `user_events` using `KafkaProducer`.

- **Cron job simulation:**  
  Events are generated and sent every 10 seconds using the `schedule` library.

---

####  How to run

Make sure Kafka is running (e.g. via Docker), then run:

```bash
python kafka_producer/scheduler.py
```

You should see messages like:

```
Sent to Kafka -> Key: {...}, Value: {...}
```
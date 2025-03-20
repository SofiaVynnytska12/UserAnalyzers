# UserAnalyzers
# Implement Data Generation and Publishing into Kafka  

## Overview  
This project implements a Kafka producer that generates synthetic user event data and publishes it to a Kafka topic (`user_events`). Events include login attempts, button clicks, search queries, and comments.  

## Project Structure  
```
UserAnalyzers/
│── kafka_producer/
│   ├── data_generator.py      # Generates random user events
│   ├── kafka_producer.py      # Publishes messages to Kafka
│   ├── scheduler.py           # Automates data generation with scheduled tasks
│── docker-compose.yml         # Kafka & Zookeeper setup
│── README.md                  # Documentation
```

## Prerequisites  
Before running the project, ensure you have the following installed:  
- Docker & Docker Compose  
- Python 3.10+  
- Required Python libraries (`kafka-python`, `schedule`)  

You can install missing dependencies using:  
```sh
pip install kafka-python schedule
```

## Setting Up Kafka  
Start the Kafka and Zookeeper services using Docker:  
```sh
docker-compose up -d
```

Verify that Kafka is running:  
```sh
docker ps
```

Ensure the Kafka topic `user_events` exists:  
```sh
docker exec -it kafka kafka-topics.sh --bootstrap-server localhost:9092 --list
```
If the topic is missing, create it manually:  
```sh
docker exec -it kafka kafka-topics.sh --bootstrap-server localhost:9092 --create --topic user_events --partitions 1 --replication-factor 1
```

## Running the Producer  
Navigate to the `kafka_producer` directory:  
```sh
cd kafka_producer
```
Run the scheduled data generator:  
```sh
python scheduler.py
```
You should see logs indicating that messages are being generated and sent to Kafka.

## Verifying Kafka Messages  
Use the Kafka console consumer to check if the messages are being received:  
```sh
docker exec -it kafka kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic user_events --from-beginning
```


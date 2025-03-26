 US-3_Implement_data_generation_and_publishing_into_Kafka
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
# Web Application Data Generator
# UserAnalyzers

## Project Description
Web Application Data Generator a system for generating, storing, and processing user activity data from a fictional web application. It simulates user actions, stores them in a database, and streams them for analysis.

## Technologies
- Python: Application logic and data generation.
- Kafka: Data streaming.
- MySQL: Data storage.
- Docker: Service containerization.
- Liquibase: Database migrations.
- JSON: Data structuring.

## Data Overview
The following user activity data will be processed:
- User logins (e.g., who logged in and when)
- Element clicks (e.g., interacting with buttons or links)
- Search queries (e.g., what users searched for)
- Comments (e.g., comment text)

The data is small, randomly generated, and sent as a stream.

## Libraries
- **Data Libraries**:
- *Random*: for generating random values ​​(e.g. timestamps, IDs)
- **Helper Libraries and Tools**:
- *kafka-python*: for integrating with Kafka and sending messages
- *json*: for encoding data into JSON format
- *datetime*: for managing timestamps in the data generation loop
- Plugins and database connectors

  ## Branch Contributions
- **US-1_Create_Readme_file**: Initial project documentation.
- **US-2_Launch_Kafka_in_Docker**: Kafka and Zookeeper setup in Docker.
- **US-3_Implement_data_generation_and_publishing_into_Kafka**: User activity data generation and streaming to Kafka.
- **US-5_Launch_Database_in_Docker**: MySQL setup in Docker with test user creation.
- **US-7_Add_migrations_for_DB_schema_creation**: Database schema migrations using Liquibase.
- **US-8_dockerize_the_application**: Application containerization with environment variable support.
  
 ## How it Works
The system periodically generates random user activity data, formats it as JSON, and sends it to a Kafka topic for further processing or analysis. Data is stored in a database with a predefined schema and can be accessed for analysis.


####  How to run

Make sure Kafka is running (e.g. via Docker), then run:

```bash
python kafka_producer/scheduler.py
```

You should see messages like:

```
Sent to Kafka -> Key: {...}, Value: {...}
```

# Web Application Data Generator
# UserAnalyzers

## Project Description
Web Application Data Generator a system for generating, storing, and processing user activity data from a fictional web application. It simulates user actions, stores them in a database, and streams them for analysis.

## Technologies
- Python: Application logic and data generation.
- Kafka: Data streaming.
- MySQL: Data storage.
- Docker: Service containerization.
- Liquibase: Database migrations.
- JSON: Data structuring.

## Data Overview
The following user activity data will be processed:
- User logins (e.g., who logged in and when)
- Element clicks (e.g., interacting with buttons or links)
- Search queries (e.g., what users searched for)
- Comments (e.g., comment text)

The data is small, randomly generated, and sent as a stream.

## Libraries
- **Data Libraries**:
- *Random*: for generating random values ​​(e.g. timestamps, IDs)
- **Helper Libraries and Tools**:
- *kafka-python*: for integrating with Kafka and sending messages
- *json*: for encoding data into JSON format
- *datetime*: for managing timestamps in the data generation loop
- Plugins and database connectors

  ## Branch Contributions
- **US-1_Create_Readme_file**: Initial project documentation.
- **US-2_Launch_Kafka_in_Docker**: Kafka and Zookeeper setup in Docker.
- **US-3_Implement_data_generation_and_publishing_into_Kafka**: User activity data generation and streaming to Kafka.
- **US-5_Launch_Database_in_Docker**: MySQL setup in Docker with test user creation.
- **US-7_Add_migrations_for_DB_schema_creation**: Database schema migrations using Liquibase.
- **US-8_dockerize_the_application**: Application containerization with environment variable support.
  
 ## How it Works
The system periodically generates random user activity data, formats it as JSON, and sends it to a Kafka topic for further processing or analysis. Data is stored in a database with a predefined schema and can be accessed for analysis.


# UserAnalyzers

## 2. Launch Kafka in Docker

### Description
This project sets up **Apache Kafka** and **Zookeeper** in Docker containers using `docker-compose.yml`.  
Kafka is used for event processing, while Zookeeper manages configuration and synchronization.

### How to Run?
1. Install **Docker** and **Docker Compose**.
2. Clone the repository:
   ```sh
   git clone https://github.com/hadupiakAA/UserAnalyzers.git
   cd UserAnalyzers
   ```
3. Make sure you are in your branch:
   ```sh
   git checkout 2.Launch-Kafka-in-Docker
   ```
4. Start Kafka and Zookeeper in Docker:
   ```sh
   docker-compose up -d
   ```
5. Verify that the containers are running:
   ```sh
   docker ps
   ```
   You should see two active containers: **kafka** and **zookeeper**.

### Kafka Verification:
1. **Create a topic in Kafka:**
   ```sh
   docker exec -it kafka kafka-topics.sh --create --topic test-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
   ```
2. **List available topics:**
   ```sh
   docker exec -it kafka kafka-topics.sh --list --bootstrap-server localhost:9092
   ```
   You should see `test-topic` in the list.

3. **Send a message to Kafka:**
   ```sh
   docker exec -it kafka kafka-console-producer.sh --broker-list localhost:9092 --topic test-topic
   ```
   Type:
   ```
   Hello, Kafka!
   ```
   and press **Enter**.

4. **Read messages from Kafka:**
   ```sh
   docker exec -it kafka kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test-topic --from-beginning
   ```
   You should see the following output:
   ```
   Hello, Kafka!
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


### Stopping the Containers:
To stop and remove Kafka and Zookeeper containers, run:
```sh
docker-compose down
```


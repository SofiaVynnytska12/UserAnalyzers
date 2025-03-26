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

### Stopping the Containers:
To stop and remove Kafka and Zookeeper containers, run:
```sh
docker-compose down
```


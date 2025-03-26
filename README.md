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

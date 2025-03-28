# UserAnalyzers


---

# Database Migrations for UserAnalyzers Project

This module implements database schema creation and test data insertion using **Liquibase** in **YAML format**.

---

##  Technologies Used

- **Liquibase** – for managing database changes
- **MySQL** – as the target database
- **YAML** – for describing database changesets
- **JDBC Driver** – MySQL Connector/J

---

##  What This Includes

1.  Liquibase configuration (`liquibase.properties`)  
2.  Database changelogs:  
   - Table creation  
   - Test data insertion  
3.  MySQL driver added to project  
4.  Documentation with setup instructions (you’re reading it!)

---

##  Database Schema

### `login_events` table

| Column     | Type        |
|------------|-------------|
| event_type | VARCHAR(50) |
| user_id    | INT         |
| username   | VARCHAR(100)|
| email      | VARCHAR(100)|
| country    | VARCHAR(50) |
| timestamp  | TIMESTAMP   |

---

### `click_events` table

| Column     | Type         |
|------------|--------------|
| event_type | VARCHAR(50)  |
| user_id    | INT          |
| element_id | VARCHAR(100) |
| page_url   | VARCHAR(200) |
| timestamp  | TIMESTAMP    |
| post_id    | INT          |

---

##  Project Structure

```  .
├── liquibase/                          
│   ├── db.changelog.yaml              
│   └── changelogs/
│       └── 001-init-and-insert.yaml   
├── libs/                               
│   └── mysql-connector-j-8.3.0.jar     
├── liquibase.properties                                          
└── README.md                            
 ```
---

##  Configuration Example (`liquibase.properties`)

```properties
changeLogFile: liquibase/db.changelog.yaml
url: jdbc:mysql://localhost:3306/UserAnalyzers
username: Analyzer
password: UA
driver: com.mysql.cj.jdbc.Driver
classpath: libs/mysql-connector-j-8.3.0.jar



##  How to Apply Migrations

1. Make sure MySQL server is running and a database named UserAnalyzers exists.
2. Open terminal in the project directory.
3. Run the following command:

liquibase update

This will:
 Create tables login_events and click_events
 Insert initial test data 


##  Sample Data Inserted

Two login_events and two click_events are inserted for testing purposes.


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

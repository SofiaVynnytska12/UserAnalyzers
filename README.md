# Web Application Data Generator

## Project Goal
This project aims to simulate a continuous stream of user activity data from a fictional web application. The goal is to generate realistic random data and send it to a processing system for further analysis, simulating the behavior of a real web application without building an actual application.

## Data Overview
The following user activity data will be processed:
- User logins (e.g., who logged in and when)
- Element clicks (e.g., interacting with buttons or links)
- Search queries (e.g., what users searched for)
- Comments (e.g., comment text)

The data is small, randomly generated, and sent as a stream.

## Technologies
- **Python** (latest versions): for random data generation and flow control
- **Kafka** (latest versions): for processing data streams and message queues
- **JSON** (standard): for structuring data in a simple, readable format
- **Docker** (latest versions): for containerizing applications and services

## Libraries
- **Data Libraries**:
- *Faker*: for generating realistic fake data (e.g. names, email addresses, countries)
- *Random*: for generating random values ​​(e.g. timestamps, IDs)
- **Helper Libraries and Tools**:
- *kafka-python*: for integrating with Kafka and sending messages
- *json*: for encoding data into JSON format
- *datetime*: for managing timestamps in the data generation loop

## How it will work
The system runs a loop that generates random data about actions user every few seconds, packages them into JSON, and sends them to a Kafka topic. From there, the data can be extracted for processing or analysis.
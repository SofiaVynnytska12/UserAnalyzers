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

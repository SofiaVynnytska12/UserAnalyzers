#Launching MySQL Docker Database on a local computer (localhost)

This is a project to launch a MySQL database in Docker, test connection, and create a test users with different levels of access.
 

## How to Run

1. **Install Docker**:  
   - Download and install Docker Desktop from [docker.com] for Linux or Windows.  
   - Launch Docker Desktop and ensure it is running.
   - If it necessary, you have to install WSL to run Docker correctly.

2. **Launch MySQL in Docker**:  
   Run the following command in PowerShell or Docker Terminal to start, check, and stop a MySQL container:
```sh
docker run -d -p 3306:3306 --name mysql-container -e MYSQL_ROOT_PASSWORD=UA -e MYSQL_DATABASE=UserAnalyzers mysql:latest
```

```sh
docker ps
```

```sh
docker stop mysql-container
```
```sh
docker start mysql-container
```
- This command uses the official MySQL image (`mysql:latest`), maps port `3306` to your localhost, sets the root password to `UA`, and creates a database named `UserAnalyzers`. 
- Docker ps checks if the container is running.
- docker stop mysql-container: To stop the running container without deleting it (you can start it again later).
- docker start mysql-container: By this command you can start your container, but in my opinion, it can be faster by starting directly again in docker desktop.

3. **Create Users**:  
Connect to MySQL as `root` to create users:
```sh
docker exec -it mysql-container mysql -uroot -pUA
```
Run SQL command from terminal (SQL_Users_Query) to create users `Analyzer` and `UserAnalyzers` with different levels of access:
- `Analyzer` has full privileges on all databases.  
- `UserAnalyzers` has privileges only on the `UserAnalyzers` database.

4. **You can also use the Docker Compose file** to lauch database directly:
- Ensure you have the `docker-compose.yml` from downloads.  
- Run the following command in PowerShell from the directory containing `docker-compose.yml`.
```sh
docker-compose up -d
```
Repeat all actions which described in the point 3

5. **Check your access for different users**:
-Run:
```sh
SHOW DATABASES;
```
- Test in on two different users.

6. **Install Python Plugin**:  
Install the required plugin in your Python environment to work with Docker MySQL Database:
```sh
pip install mysql-connector-python
```
7. **Run the python Script**:  
Run the Python script with working container and MySQL Database to test the connection (downloadable):
**python_Plugin.py**
## What the Script Does
- The script (`Plugin.py`) connects to MySQL on `localhost:3306` as `Analyzer` and `UserAnalyzers`.  
- It prints the databases each user can see, verifying the connection and user setup.

## Notes
- The database is only accessible from your local machine and local programming environments (`localhost:3306`). 
- Do not forget to close your container or connections after your session - it takes a lot of RAM.
- Local services and databases is shutting down when local machine shuts down.

# Dockerized Python Applications

This project contains test Python application (`test.py`) that demonstrate environment variable injection within a Docker container.
Let's see how it works!

## Features
- **Dockerfile** - to containerize the application / applications.
- **Docker Compose** configuration for easy setup and running (you need to use just one line of code to build and start your Docker).
- **Environment Variable** (`TEST_VARIABLE`) to test dynamic values.
- **Script Execution** via `SCRIPT_NAME` variable.

## Prerequisites
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Project Structure
```
.
├── test.py             # Test application
├── Dockerfile          # Docker configuration file
├── docker-compose.yml  # Docker Compose configuration
├── .dockerignore       # Files to ignore in Docker builds
├── .env                # Environment variable definitions
└── README.md           # This documentation
```

## Running the Application

### 1. Build and Run with Docker Compose
```sh
docker-compose up --build
```
This will build the container and start it using environment variables defined in `.env`.

### 2. Running with Custom Environment Variables
To override default values, modify `.env` or use:
```sh
docker-compose up --build -d
TEST_VARIABLE="Custom value" SCRIPT_NAME=test.py docker-compose up
```

### 3. Running a Container Manually
If you prefer not to use Docker Compose:
```sh
docker build -t my_python_app .
docker run --rm -e TEST_VARIABLE="Custom message" -e SCRIPT_NAME=test.py my_python_app
```

## Expected Output
When the container starts, you should see:
```
You are inside the container and it's test! The TEST_VARIABLE is: TEST_VARIABLE
```

## Notes
- By default, `test.py` runs (as set in `.env`).
- Modify `SCRIPT_NAME` to run a different script.
- Change `TEST_VARIABLE` for custom messages.
- Hope this is informative Readme file

## Cleanup
To stop and remove containers:
```sh
docker-compose down
```
To remove images:
```sh
docker rmi my_python_app
```

## License
MIT License




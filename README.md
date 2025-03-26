# Dockerized Python Applications

This project contains a test Python application (`test.py`) that demonstrates how to pass environment variables into a Docker container. It's a simple example, but it helps understand the basics of working with Docker.

## What's Included
- **Dockerfile** — used to build a container with the application.
- **Docker Compose** — makes it easy to run the project (just one command, and everything works!).
- **Environment Variables** — we use `TEST_VARIABLE` to pass dynamic values.
- **Script Execution** — you can specify which script to run using `SCRIPT_NAME`.

## Requirements
Before running the project, make sure you have installed:
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Project Structure
```
.
├── test.py             # Test Python script
├── Dockerfile          # Configuration for building the container
├── docker-compose.yml  # File for running with Docker Compose
├── .dockerignore       # File to exclude unnecessary files from the container
├── .env                # File with environment variables
└── README.md           # This documentation
```

## How to Run

### 1. Run with Docker Compose
```sh
docker-compose up --build
```
This command will build the container and run it using environment variables from `.env`.

### 2. Run with Custom Environment Variables
You can modify `.env` or pass variables directly:
```sh
docker-compose up --build -d
TEST_VARIABLE="TEST_VAR" SCRIPT_NAME=test.py docker-compose up
```

### 3. Run Manually Without Docker Compose
If you prefer not to use Compose:
```sh
docker build -t my_python_app .
docker run --rm -e TEST_VARIABLE="SOME_VARIABLE" -e SCRIPT_NAME=test.py my_python_app
```

## Expected Console Output
When the container starts, you should see something like:
```
You are inside the container, and this is a test! TEST_VARIABLE value: TEST_VARIABLE
```

## Useful Notes
- By default, `test.py` runs, but you can specify a different script using `SCRIPT_NAME`.
- `TEST_VARIABLE` can be changed to display custom messages.
- It's quite simple but helps to grasp Docker basics.

## How to Stop and Remove Containers
To stop and remove the container:
```sh
docker-compose down
```
If you need to remove the image itself:
```sh
docker rmi my_python_app
```

## License
MIT License

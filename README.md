# FastAPI, Poetry, and Docker Demo
This project demonstrates a simple FastAPI application managed with Poetry, containerized using Docker, and tested with Pytest. It provides a robust and reproducible setup for modern Python API development.

### Features
**FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.

**Poetry**: An excellent tool for dependency management and packaging in Python. It handles virtual environments, dependency resolution, and project building seamlessly.

**Docker**: Containerizes the application for consistent and reproducible deployments across different environments. It uses multi-stage builds to create lean production images.

**Pytest & httpx**: A powerful testing framework for Python, used with httpx for making asynchronous HTTP requests to test the API endpoints.

### Prerequisites
Before you get started, make sure you have the following installed on your system:

Python 3.11+: The project is configured for Python 3.11.

Poetry: You can find installation instructions here.

Docker: You can find installation instructions here.

### Getting Started
Follow these steps to get the project up and running locally or via Docker.

1. Clone the Repository
First, clone this repository to your local machine and navigate into the project directory:

**Bash**
```
git clone https://github.com/your-username/fastapi-poetry-docker.git
cd fastapi-poetry-docker
```
2. Local Development Setup (Recommended for Development)

This method runs the application directly on your machine, with Poetry managing your project's dependencies.

a. Set up the Python Environment:
Poetry will create a virtual environment and install all project dependencies, including development tools like pytest and httpx. Ensure you have Python 3.11+ installed on your system and available to Poetry.

**Bash**
```
# If you have multiple Python versions, tell Poetry to use 3.11
# (e.g., if you installed via pyenv, this might be 'poetry env use 3.11.0')
poetry env use python3.11
# Install project dependencies
poetry install
```
b. Run the API Locally:
You can run the FastAPI application using uvicorn via Poetry's run command.

**Bash**
```
poetry run uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
```
The `--reload` flag is handy for development, as it automatically restarts the server when you make code changes.

c. Access the API:
Once the server's running, open your web browser or use curl:

Root Endpoint: `http://localhost:8000/`

Example Item Endpoint: `http://localhost:8000/items/123?q=test`

Interactive API Docs (Swagger UI): `http://localhost:8000/docs`

Alternative API Docs (ReDoc): `http://localhost:8000/redoc`

3. Running with Docker (Recommended for Deployment)
This method builds a production-ready Docker image of your FastAPI application, ensuring consistent behavior across environments.

a. Build the Docker Image:
Make sure you're in the root directory of the project (where Dockerfile is located).

**Bash**
```
docker build -t fastapi-poetry-docker:latest .
This command uses a multi-stage build to create a small, optimized image containing only your application and its production dependencies.
```
b. Run the Docker Container:
Map port 8000 on your host machine to port 8000 inside the container.

**Bash**
```
docker run -p 8000:8000 --name fastapi-demo-container fastapi-poetry-docker:latest
```
The `--name` flag gives your container a friendly name.

c. Access the API:
Just like with local development, you can access the API in your browser:

Root Endpoint: `http://localhost:8000/`
Interactive API Docs (Swagger UI): `http://localhost:8000/docs`

d. Stop and Remove the Docker Container:
When you're finished, stop and remove the container:

**Bash**
```
docker stop fastapi-demo-container
docker rm fastapi-demo-container
```

4. Running Tests
To run the unit and integration tests for the API, use Poetry's run command with pytest:

**Bash**
```
poetry run pytest
```
This will execute the tests defined in the tests/ directory.
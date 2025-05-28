# Dockerfile

# --- Stage 1: Builder Stage ---
FROM python:3.11-slim-buster AS builder

ENV POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

ENV PATH="$POETRY_HOME/bin:$PATH"

RUN pip install "poetry==1.8.2" # Pin Poetry version

WORKDIR /app

# Copy only the dependency files to leverage Docker layer caching
COPY pyproject.toml poetry.lock* ./

# Install project dependencies.
# We include gunicorn, uvicorn, and fastapi.
RUN poetry install --no-root --without dev

# --- Stage 2: Runtime Stage ---
FROM python:3.11-slim-buster AS runtime

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Set the path to the virtual environment created in the builder stage
ENV VIRTUAL_ENV="/app/.venv"
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /app

# Copy the virtual environment from the builder stage
COPY --from=builder /app/.venv /app/.venv

# Copy your actual application code
COPY src/ ./src/

# Expose the port FastAPI will listen on (default is 8000)
EXPOSE 8000

# Command to run your FastAPI application using Gunicorn with Uvicorn workers.
# -w N: Number of worker processes (N = 2 * CPU_CORES + 1 is a common heuristic, adjust as needed)
# -k uvicorn.workers.UvicornWorker: Specifies the Uvicorn worker class for Gunicorn
# main:app: Refers to the `app` object in `src/main.py` (module:variable)
# --bind 0.0.0.0:8000: Binds the server to all network interfaces on port 8000
CMD ["gunicorn", "src.main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]
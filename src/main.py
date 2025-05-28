# fastapi-poetry-docker/src/main.py

from fastapi import FastAPI

app = FastAPI(title="FastAPI Poetry Docker Demo")

@app.get("/")
async def read_root():
    """
    A simple root endpoint that returns a greeting.
    """
    return {"message": "Hello from FastAPI, Poetry, and Docker!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    """
    An endpoint to demonstrate path and query parameters.
    """
    return {"item_id": item_id, "q": q}
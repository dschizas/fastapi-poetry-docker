# tests/test_main.py

import pytest
from httpx import AsyncClient

# Import the FastAPI app instance from your main.py
# Assuming your main.py is in the 'src' directory
from src.main import app

# Pytest fixture to create an async test client for FastAPI
# This allows us to test the FastAPI app directly without starting a server
@pytest.fixture(scope="module")
async def async_client():
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client

# Test for the root endpoint
@pytest.mark.asyncio
async def test_read_root(async_client: AsyncClient):
    response = await async_client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello from FastAPI, Poetry, and Docker!"}

# Test for the items endpoint without a query parameter
@pytest.mark.asyncio
async def test_read_item_no_query(async_client: AsyncClient):
    item_id = 42
    response = await async_client.get(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json() == {"item_id": item_id, "q": None}

# Test for the items endpoint with a query parameter
@pytest.mark.asyncio
async def test_read_item_with_query(async_client: AsyncClient):
    item_id = 99
    query_param = "test_query"
    response = await async_client.get(f"/items/{item_id}?q={query_param}")
    assert response.status_code == 200
    assert response.json() == {"item_id": item_id, "q": query_param}

# Test for a non-existent endpoint (expect 404)
@pytest.mark.asyncio
async def test_read_non_existent_path(async_client: AsyncClient):
    response = await async_client.get("/non-existent-path")
    assert response.status_code == 404
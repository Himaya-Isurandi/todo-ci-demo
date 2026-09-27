import os
import pytest
from fastapi.testclient import TestClient
from main import app, todos

client = TestClient(app)

@pytest.fixture(autouse=True)
def clear_todos():
    todos.clear()
    yield

def test_create_todo():
    response = client.post("/todos/", json={"id": 1, "title": "Buy milk"})
    assert response.status_code == 200
    assert response.json()["title"] == "Buy milk"
    
def test_list_todos():
    client.post("/todos/", json={"id": 1, "title": "Buy milk"})
    client.post("/todos/", json={"id": 2, "title": "Buy eggs"})
    response = client.get("/todos/")
    assert response.status_code == 200
    assert len(response.json()) == 2

def test_secret_env_var():
    # Simulate a required environment variable (secret)
    secret = os.getenv("MY_SECRET_KEY")
    assert secret is not None, "MY_SECRET_KEY environment variable is not set"
    # Ensure it's not empty, but we don't print it
    assert len(secret) > 0

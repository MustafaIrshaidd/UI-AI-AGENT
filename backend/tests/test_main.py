import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    """Test the root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "Hello from FastAPI with Poetry!" in data["message"]

def test_health_check():
    """Test the health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    assert data["status"] == "healthy"
    assert "environment" in data

def test_cors_headers():
    """Test that CORS headers are properly set"""
    response = client.options("/")
    assert response.status_code == 200
    # CORS headers should be present
    assert "access-control-allow-origin" in response.headers 
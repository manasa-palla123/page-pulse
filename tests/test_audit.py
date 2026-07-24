from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "running"


def test_invalid_url():
    response = client.post(
        "/audit/",
        json={"url": "invalid-url"}
    )

    assert response.status_code == 422


def test_valid_url():
    response = client.post(
        "/audit/",
        json={"url": "https://google.com"}
    )

    assert response.status_code == 200

    data = response.json()

    assert data["success"] is True
    assert "status_code" in data
    assert "response_time_ms" in data
    assert "request_id" in data
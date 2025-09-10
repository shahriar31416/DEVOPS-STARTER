from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_healthz():
    r = client.get("/healthz")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_create_item():
    r = client.post("/items", json={"id": 1, "name": "alpha"})
    assert r.status_code == 200
    data = r.json()
    assert data["message"] == "created"
    assert data["item"]["name"] == "alpha"

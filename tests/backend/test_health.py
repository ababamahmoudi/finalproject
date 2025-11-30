# tests/backend/test_health.py
from fastapi.testclient import TestClient
from applications.backend.app.main import app

client = TestClient(app)

def test_health():
    resp = client.get("/health")
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "ok"
    assert data["service"] == "backend"

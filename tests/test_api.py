from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_health():
    res = client.get("/")
    assert res.status_code == 200

def test_predict():
    payload = {
        "OP_CARRIER": "AA",
        "ORIGIN": "JFK",
        "DEST": "LAX",
        "CRS_DEP_TIME": 800,
        "CRS_ARR_TIME": 1142,
        "DISTANCE": 2475.0
    }
    res = client.post("/predict", json=payload)
    assert res.status_code == 200
    assert "prediction" in res.json()
from fastapi.testclient import TestClient
import sys
import os

# This lets Python find your api folder
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from api.main import app

client = TestClient(app)

# Test 1 - Health check
def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

# Test 2 - Valid prediction returns 200
def test_predict_valid_input():
    payload = {
        "revolving_utilization": 0.5,
        "age": 45,
        "times_30_59_days_late": 0,
        "debt_ratio": 0.3,
        "monthly_income": 6000,
        "open_credit_lines": 8,
        "times_90_days_late": 0,
        "real_estate_loans": 1,
        "times_60_89_days_late": 0,
        "dependents": 2
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "default_prediction" in data
    assert "default_probability" in data
    assert "risk_level" in data
    assert data["default_prediction"] in [0, 1]
    assert 0 <= data["default_probability"] <= 1
    assert data["risk_level"] in ["Low", "Medium", "High"]

# Test 3 - High risk applicant
def test_predict_high_risk():
    payload = {
        "revolving_utilization": 0.99,
        "age": 25,
        "times_30_59_days_late": 5,
        "debt_ratio": 0.9,
        "monthly_income": 1000,
        "open_credit_lines": 15,
        "times_90_days_late": 10,
        "real_estate_loans": 0,
        "times_60_89_days_late": 5,
        "dependents": 4
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["default_prediction"] == 1  # should predict default

# Test 4 - Missing field returns 422 error
def test_predict_missing_field():
    payload = {
        "age": 45,
        "monthly_income": 6000
        # missing all other required fields
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 422  # validation error

# Test 5 - Model info endpoint
def test_model_info():
    response = client.get("/model/info")
    assert response.status_code == 200
    data = response.json()
    assert "model_type" in data
    assert data["features"] == 10
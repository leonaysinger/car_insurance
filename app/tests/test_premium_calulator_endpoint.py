import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.fixture
def car_details():
    return {
        "make": "Toyota",
        "model": "Corolla",
        "year": 2020,
        "value": 20000.0,
        "deductible_percentage": 0.1,
        "broker_fee": 50.0,
        "registration_location": "New York"
    }

def test_calculate_premium_success(car_details):
    response = client.post("/calculate-premium/", json=car_details)
    assert response.status_code == 200  # Successful response
    data = response.json()

    # Validate response schema
    assert "applied_rate" in data
    assert "policy_limit" in data
    assert "calculated_premium" in data
    assert "deductible_value" in data

    # Check response values are reasonable
    assert data["applied_rate"] == 0.035
    assert data["policy_limit"] == 18000
    assert data["calculated_premium"] == 680.0000000000001
    assert data["deductible_value"] == 1800

def test_calculate_premium_missing_data():
    incomplete_data = {
        "make": "Toyota",
        "model": "Corolla",
        # Missing required fields
    }
    response = client.post("/calculate-premium/", json=incomplete_data)
    assert response.status_code == 422

def test_calculate_premium_invalid_data():
    invalid_data = {
        "make": "Toyota",
        "model": "Corolla",
        "year": "not_a_year",  # Invalid year format
        "value": "invalid_value",  # Should be a float
        "deductible_percentage": 0.1,
        "broker_fee": 50.0,
        "registration_location": "New York"
    }
    response = client.post("/calculate-premium/", json=invalid_data)
    assert response.status_code == 422

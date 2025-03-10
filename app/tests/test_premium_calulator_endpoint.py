import pytest
from fastapi.testclient import TestClient

from app.api.endpoints.premium_calculator import router
from app.main import app

app.include_router(router)

client = TestClient(app)


@pytest.fixture
def valid_car_details():
    return {
        "make": "Toyota",
        "model": "Corolla",
        "year": 2015,
        "value": 20000.0,
        "deductible_percentage": 0.1,
        "broker_fee": 50.0,
        "registration_location": "New York"
    }


@pytest.fixture
def invalid_car_details():
    return {
        "make": "Toyota",
        "model": "Corolla",
        "year": 2015,
        "value": -5000.0,  # Invalid: Negative car value
        "deductible_percentage": 0.1,
        "broker_fee": 50.0,
        "registration_location": "New York"
    }


@pytest.fixture
def car_details_no_location():
    return {
        "make": "Honda",
        "model": "Civic",
        "year": 2020,
        "value": 25000.0,
        "deductible_percentage": 0.2,
        "broker_fee": 75.0,
        "registration_location": None
    }


def test_calculate_premium_success(valid_car_details):
    response = client.post("/calculate-premium/", json=valid_car_details)

    assert response.status_code == 200
    data = response.json()

    assert "applied_rate" in data
    assert "policy_limit" in data
    assert "calculated_premium" in data
    assert "deductible_value" in data

    assert data["applied_rate"] > 0
    assert data["policy_limit"] > 0
    assert data["calculated_premium"] > 0
    assert data["deductible_value"] >= 0


def test_calculate_premium_invalid_input(invalid_car_details):
    response = client.post("/calculate-premium/", json=invalid_car_details)
    assert response.status_code == 422


def test_calculate_premium_without_location(car_details_no_location):
    response = client.post("/calculate-premium/", json=car_details_no_location)

    assert response.status_code == 200
    data = response.json()

    assert "applied_rate" in data
    assert "policy_limit" in data
    assert "calculated_premium" in data
    assert "deductible_value" in data

    assert data["applied_rate"] > 0
    assert data["policy_limit"] > 0
    assert data["calculated_premium"] > 0
    assert data["deductible_value"] >= 0

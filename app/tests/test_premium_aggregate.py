import pytest

from app.core.aggregate.premium import Premium
from app.core.entities.car import Car
from app.core.entities.policy import Policy
from app.core.value_objects.deductible import Deductible
from app.core.value_objects.location import Location
from app.core.value_objects.rate import Rate

@pytest.fixture
def car():
    return Car(make="Toyota", model="Corolla", year=2012, value=100000.0)

@pytest.fixture
def policy():
    return Policy(deductible_percentage=0.1, broker_fee=50.0, registration_location=None)

@pytest.fixture
def rate():
    return Rate(age_rate=0.05, value_rate=0.05)

@pytest.fixture
def deductible():
    return Deductible(percentage=0.1)

@pytest.fixture
def location():
    return Location(name="New York", risk_factor=0.01)


def test_calculate_premium_with_location(car, policy, rate, deductible, location):
    premium = Premium(car, policy, rate, deductible, location)
    assert premium.calculate_premium() == 10503.5

def test_calculate_rate_with_location(car, policy, rate, deductible, location):
    premium = Premium(car, policy, rate, deductible, location)
    assert premium.calculate_rate() == 0.11615

def test_calculate_rate_without_location(car, policy, rate, deductible):
    premium = Premium(car, policy, rate, deductible)
    assert premium.calculate_rate() == 0.115

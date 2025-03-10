from app.core.services.premium_calculator_service import calculate_premium_data
from app.core.dto.dtos import CarDetails, PremiumResponse


sample_car_details = CarDetails(
    make="Toyota",
    model="Corolla",
    year=2012,
    value=100000.0,
    deductible_percentage=0.1,
    broker_fee=50.0,
    registration_location="New York"
)


def test_calculate_premium_valid_input():
    response = calculate_premium_data(sample_car_details)

    # Assertions
    assert response is not None
    assert isinstance(response, PremiumResponse)
    assert response.applied_rate == 0.115
    assert response.policy_limit == 90000.0
    assert response.calculated_premium == 10400
    assert response.deductible_value == 9000


def test_calculate_premium_without_location():
    car_details_no_location = CarDetails(
        make="Toyota",
        model="Corolla",
        year=2012,
        value=100000.0,
        deductible_percentage=0.1,
        broker_fee=50.0,
    )

    response = calculate_premium_data(car_details_no_location)

    assert response is not None
    assert response.applied_rate == 0.115
    assert response.policy_limit == 90000.0
    assert response.calculated_premium == 10400
    assert response.deductible_value == 9000

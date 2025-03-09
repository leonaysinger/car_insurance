from fastapi import HTTPException

from app.core.aggregate.premium import Premium
from app.core.dto.dtos import CarDetails, PremiumResponse
from app.core.entities.car import Car
from app.core.entities.policy import Policy
from app.core.value_objects.deductible import Deductible
from app.core.value_objects.location import Location
from app.core.value_objects.policy_limit import PolicyLimit
from app.core.value_objects.rate import Rate


def calculate_premium(car_details: CarDetails):
    try:
        # Create the car, policy, deductible, and location instances from input data
        car = Car(make=car_details.make, model=car_details.model, year=car_details.year, value=car_details.value)
        policy = Policy(deductible_percentage=car_details.deductible_percentage, broker_fee=car_details.broker_fee,
                        registration_location=car_details.registration_location)
        deductible = Deductible(percentage=car_details.deductible_percentage)

        location = None
        if car_details.registration_location:
            location = Location(name=car_details.registration_location)

        # Calculate the premium
        premium_calculator = Premium(car=car, policy=policy, rate=Rate(0.05, 0.05), deductible=deductible,
                                     location=location)
        calculated_premium = premium_calculator.calculate_premium()

        # Calculate the policy limit
        policy_limit_calculator = PolicyLimit(car_value=car.value, coverage_percentage=1.0,
                                              deductible_percentage=policy.deductible_percentage)
        final_policy_limit = policy_limit_calculator.calculate_policy_limit()

        # Calculate the deductible value
        deductible_value = policy_limit_calculator.calculate_policy_limit() * policy.deductible_percentage

        return PremiumResponse(
            applied_rate=premium_calculator.calculate_rate(),
            policy_limit=final_policy_limit,
            calculated_premium=calculated_premium,
            deductible_value=deductible_value
        )

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
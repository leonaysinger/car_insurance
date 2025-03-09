from datetime import datetime
from typing import Optional

from app.core.entities.car import Car
from app.core.entities.policy import Policy
from app.core.value_objects.deductible import Deductible
from app.core.value_objects.location import Location
from app.core.value_objects.rate import Rate


class Premium:
    def __init__(self, car: Car, policy: Policy, rate: Rate, deductible: Deductible,
                 location: Optional[Location] = None):
        self.car = car
        self.policy = policy
        self.rate = rate
        self.deductible = deductible
        self.location = location
        self.limit_Value_car_price = 10000

    def calculate_premium(self) -> float:
        # Calculate rate from car age and value
        applied_rate = self.calculate_rate()

        # Base premium
        base_premium = self.car.value * applied_rate

        # Deductible discount
        deductible_discount = self.deductible.calculate_deductible_discount(base_premium)

        # Final premium
        premium = base_premium - deductible_discount + self.policy.broker_fee
        return premium

    def calculate_rate(self) -> float:
        current_year = datetime.now().year
        age_rate = (current_year - self.car.year) * 0.5 / 100  # Example: 0.5% for each year
        value_rate = (self.car.value / self.limit_Value_car_price) * 0.5 / 100  # 0.5% for every $10,000 of car value
        rate = Rate(age_rate, value_rate)

        if self.location:
            # Adjust rate based on location risk factor
            rate = Location(self.location.name, self.location.risk_factor).adjust_rate(rate.calculate_applied_rate())
        else:
            rate = rate.calculate_applied_rate()

        return rate
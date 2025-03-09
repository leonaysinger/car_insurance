from dataclasses import dataclass

@dataclass(frozen=True)
class PolicyLimit:
    car_value: float
    coverage_percentage: float
    deductible_percentage: float

    def calculate_policy_limit(self) -> float:
        # Base policy limit is car value * coverage percentage
        base_policy_limit = self.car_value * self.coverage_percentage

        # Deductible value
        deductible_value = base_policy_limit * self.deductible_percentage

        # Final policy limit
        final_policy_limit = base_policy_limit - deductible_value
        return final_policy_limit

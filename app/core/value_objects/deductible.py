from dataclasses import dataclass

@dataclass(frozen=True)
class Deductible:
    percentage: float

    def calculate_deductible_discount(self, base_premium: float) -> float:
        return base_premium * self.percentage

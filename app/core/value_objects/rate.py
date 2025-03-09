from dataclasses import dataclass

@dataclass(frozen=True)
class Rate:
    age_rate: float
    value_rate: float
    geographic_adjustment: float = 0.0

    def calculate_applied_rate(self) -> float:
        return self.age_rate + self.value_rate + self.geographic_adjustment

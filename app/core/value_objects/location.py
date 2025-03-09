from dataclasses import dataclass

@dataclass(frozen=True)
class Location:
    name: str
    risk_factor: float = 0.0  # Between -2% to +2%

    def adjust_rate(self, rate: float) -> float:
        return rate + (rate * self.risk_factor)

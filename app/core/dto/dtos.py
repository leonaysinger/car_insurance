from pydantic import BaseModel


class CarDetails(BaseModel):
    make: str
    model: str
    year: int
    value: float
    deductible_percentage: float
    broker_fee: float
    registration_location: str = None


class PremiumResponse(BaseModel):
    applied_rate: float
    policy_limit: float
    calculated_premium: float
    deductible_value: float

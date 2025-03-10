from pydantic import BaseModel, conint, confloat, constr
from typing import Optional


class CarDetails(BaseModel):
    make: constr(min_length=1, max_length=50)
    model: constr(min_length=1, max_length=50)
    year: conint(ge=1886, le=2100)
    value: confloat(ge=0)
    deductible_percentage: confloat(ge=0, le=1)
    broker_fee: confloat(ge=0)
    registration_location: Optional[constr(min_length=1, max_length=100)]

    class Config:
        schema_extra = {
            "example": {
                "make": "Toyota",
                "model": "Corolla",
                "year": 2020,
                "value": 20000.0,
                "deductible_percentage": 0.1,
                "broker_fee": 50.0,
                "registration_location": "New York"
            }
        }


class PremiumResponse(BaseModel):
    applied_rate: float
    policy_limit: float
    calculated_premium: float
    deductible_value: float

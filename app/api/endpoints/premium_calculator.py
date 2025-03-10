from fastapi import APIRouter, HTTPException

from app.core.dto.dtos import PremiumResponse, CarDetails
from app.core.services.premium_calculator_service import calculate_premium_data

router = APIRouter()

@router.post("/calculate-premium/", response_model=PremiumResponse)
async def calculate_premium(car_details: CarDetails):
    try:
        return calculate_premium_data(car_details)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

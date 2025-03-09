from pydantic import BaseModel
from typing import Optional
from uuid import uuid4

class Policy(BaseModel):
    id: str = str(uuid4())  # Unique identifier for the policy
    deductible_percentage: float
    broker_fee: float
    registration_location: Optional[str] = None

    def update_broker_fee(self, new_fee: float):
        """Example method to update broker fee as part of the policy lifecycle"""
        self.broker_fee = new_fee

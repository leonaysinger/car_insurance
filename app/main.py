from fastapi import FastAPI
from app.api.endpoints.premium_calculator import router as premium_routes

app = FastAPI()

app.include_router(premium_routes)

from dotenv import load_dotenv
from fastapi import FastAPI

from app.api.endpoints.premium_calculator import router as premium_routes

load_dotenv()
app = FastAPI()

app.include_router(premium_routes)


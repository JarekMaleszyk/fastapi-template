from fastapi import FastAPI
from app.routes import basket

app = FastAPI(title="My FastAPI PostgreSQL App")

app.include_router(basket.router, prefix="/basket", tags=["Basket"])
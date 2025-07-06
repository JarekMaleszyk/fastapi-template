from fastapi import FastAPI
from contextlib import asynccontextmanager
from basket-api.app.core import config, logging
from basket-api.app.db.database import init_db
from basket-api.app.routers.v1 import users, items

@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.setup_logging()
    await init_db()
    yield

app = FastAPI(
    title="basket-api",
    version="0.1.0",
    description="A FastAPI project",
    lifespan=lifespan
)

app.include_router(users.router, prefix="/api/v1")
app.include_router(items.router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to basket-api!"}
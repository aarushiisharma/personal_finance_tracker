from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import transactions
from .db import get_client
from .core.config import settings

from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # create client and ensure indexes
    client = get_client()
    db = client[settings.mongo_db]
    # ensure index on date and category and type
    await db["transactions"].create_index("date")
    await db["transactions"].create_index("category")
    await db["transactions"].create_index("type")
    yield

app = FastAPI(title="Personal Finance Tracker", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to specific domains in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# include routers
app.include_router(transactions.router)

@app.get("/")
async def root():
    return {"message": "Personal Finance Tracker API running"}

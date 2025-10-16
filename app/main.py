from fastapi import FastAPI
from .routes import transactions
from .db import get_client
from .core.config import settings

app = FastAPI(title="Personal Finance Tracker")

# include routers
app.include_router(transactions.router)

@app.on_event("startup")
async def startup_db():
    # create client and ensure indexes
    client = get_client()
    db = client[settings.mongo_db]
    # ensure index on date and category and type
    await db["transactions"].create_index("date")
    await db["transactions"].create_index("category")
    await db["transactions"].create_index("type")

@app.get("/")
async def root():
    return {"message": "Personal Finance Tracker API running"}

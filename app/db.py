from motor.motor_asyncio import AsyncIOMotorClient
from .core.config import settings

client: AsyncIOMotorClient | None = None
db = None

def get_client():
    global client, db
    if client is None:
        client = AsyncIOMotorClient(settings.mongo_uri)
        db = client[settings.mongo_db]
    return client

def get_db():
    global db
    if db is None:
        get_client()
    return db

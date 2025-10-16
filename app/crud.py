from bson import ObjectId
from .db import get_db
from .models import TransactionCreate, TransactionUpdate
from datetime import datetime
from typing import List
from pymongo import DESCENDING

def txn_collection():
    return get_db()["transactions"]

async def create_transaction(txn: TransactionCreate) -> dict:
    doc = txn.dict()
    # ensure datetime stored as ISODate
    result = await txn_collection().insert_one(doc)
    doc["_id"] = result.inserted_id
    return doc

async def get_transaction(txn_id: str) -> dict | None:
    doc = await txn_collection().find_one({"_id": ObjectId(txn_id)})
    return doc

async def list_transactions(limit: int = 100, skip: int = 0) -> List[dict]:
    cursor = txn_collection().find().sort("date", DESCENDING).skip(skip).limit(limit)
    return [d async for d in cursor]

async def update_transaction(txn_id: str, data: TransactionUpdate) -> dict | None:
    update_data = {k: v for k, v in data.dict().items() if v is not None}
    if not update_data:
        return await get_transaction(txn_id)
    res = await txn_collection().find_one_and_update(
        {"_id": ObjectId(txn_id)},
        {"$set": update_data},
        return_document=True
    )
    return res

async def delete_transaction(txn_id: str) -> bool:
    res = await txn_collection().delete_one({"_id": ObjectId(txn_id)})
    return res.deleted_count == 1

# Aggregation examples:
async def monthly_summary(year: int, month: int):
    # returns total income and expense for given month
    from calendar import monthrange
    start = datetime(year, month, 1)
    end = datetime(year, month, monthrange(year, month)[1], 23, 59, 59)
    pipeline = [
        {"$match": {"date": {"$gte": start, "$lte": end}}},
        {"$group": {"_id": "$type", "total": {"$sum": "$amount"}}}
    ]
    cursor = txn_collection().aggregate(pipeline)
    return [d async for d in cursor]

async def category_totals(year: int, month: int):
    from calendar import monthrange
    start = datetime(year, month, 1)
    end = datetime(year, month, monthrange(year, month)[1], 23, 59, 59)
    pipeline = [
        {"$match": {"date": {"$gte": start, "$lte": end}}},
        {"$group": {"_id": {"category": "$category", "type": "$type"}, "total": {"$sum": "$amount"}}},
        {"$sort": {"total": -1}}
    ]
    cursor = txn_collection().aggregate(pipeline)
    return [d async for d in cursor]

from fastapi import APIRouter, HTTPException, status
from typing import List
from ..models import TransactionCreate, TransactionInDB, TransactionUpdate
from .. import crud
from bson import ObjectId

router = APIRouter(prefix="/transactions", tags=["transactions"])

def _to_response(doc: dict) -> TransactionInDB:
    return TransactionInDB(
        id=str(doc["_id"]),
        amount=doc["amount"],
        category=doc["category"],
        note=doc.get("note"),
        date=doc["date"],
        type=doc["type"]
    )

@router.post("/", response_model=TransactionInDB, status_code=status.HTTP_201_CREATED)
async def create(txn: TransactionCreate):
    doc = await crud.create_transaction(txn)
    return _to_response(doc)

@router.get("/", response_model=List[TransactionInDB])
async def list_all(limit: int = 100, skip: int = 0):
    docs = await crud.list_transactions(limit=limit, skip=skip)
    return [_to_response(d) for d in docs]

@router.get("/{txn_id}", response_model=TransactionInDB)
async def get_txn(txn_id: str):
    try:
        doc = await crud.get_transaction(txn_id)
    except Exception:
        doc = None
    if not doc:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return _to_response(doc)

@router.put("/{txn_id}", response_model=TransactionInDB)
async def update(txn_id: str, data: TransactionUpdate):
    doc = await crud.update_transaction(txn_id, data)
    if not doc:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return _to_response(doc)

@router.delete("/{txn_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(txn_id: str):
    ok = await crud.delete_transaction(txn_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return

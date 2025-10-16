from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class TransactionBase(BaseModel):
    amount: float = Field(..., gt=0)
    category: str
    note: Optional[str] = None
    date: datetime
    type: str = Field(..., regex="^(expense|income)$")  # enforce type

class TransactionCreate(TransactionBase):
    pass

class TransactionUpdate(BaseModel):
    amount: Optional[float] = Field(None, gt=0)
    category: Optional[str] = None
    note: Optional[str] = None
    date: Optional[datetime] = None
    type: Optional[str] = Field(None, regex="^(expense|income)$")

class TransactionInDB(TransactionBase):
    id: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

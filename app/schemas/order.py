from pydantic import BaseModel
from typing import List, Optional
from decimal import Decimal
from datetime import datetime
from app.schemas.oder_item import OrderItemCreate, OrderItem

class OrderCreate(BaseModel):
    user_id: int
    phonenumber: Optional[str]
    address: Optional[str]
    note: Optional[str]=None
    order_items: List[OrderItemCreate]

class Order(BaseModel):
    id: int
    user_id: int
    phonenumber: Optional[str]
    address: Optional[str]
    note: Optional[str]
    total_amount: Decimal
    status: str
    created_at: datetime
    order_items: List[OrderItem]

    class Config:
        orm_mode = True


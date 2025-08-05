from pydantic import BaseModel
from typing import Optional
from decimal import Decimal


class OrderItemBase(BaseModel):
    
    quantity:int
    price:Decimal
    
    product_id:Optional[int]
class OrderItemCreate(OrderItemBase):
    pass


class OrderItem(OrderItemBase):
    id: int

    class Config:
        from_atrribute = True
  
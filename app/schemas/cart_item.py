from pydantic import BaseModel
from typing import Optional
from app.schemas.product import ProductOut

class CartItemBase(BaseModel):
    user_id: Optional[int]
    product_id: Optional[int]
    quantity: Optional[int] = 1

class CartItemCreate(CartItemBase):
    pass

class CartItemRead(CartItemBase):
    id: int
    product:ProductOut

    class Config:
        from_attribute = True

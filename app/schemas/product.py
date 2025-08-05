from pydantic import BaseModel
from typing import Optional
class ProductBase(BaseModel):
    name: str
    price:float
    description:Optional[str]=None
    stock_quantity:Optional[int]=0
    image_url: Optional[str] = None
    category_id:Optional[int]=None
class ProductCreate(ProductBase):
    pass
class Product(ProductBase):
    id: int

    class Config:
        from_attribute = True

class ProductOut(BaseModel):
    name:str
    price:float
    image_url:str
    class Config:
        from_attribute=True
from pydantic import BaseModel
from typing import Optional
from app.schemas.product import Product
class FavoriteOut(BaseModel):
    id:int
   
    product: Product
    class Config:
        from_attribute:True


class FavoriteBase(BaseModel):
    user_id:int
    product_id:int
class FavoriteCreate(FavoriteBase):
    pass
class Favourite(FavoriteBase):
    id:int
    class Config:
        from_attribute=True

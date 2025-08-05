from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserInfo(BaseModel):
    name: str

    class Config:
        orm_mode = True


class ReviewBase(BaseModel):
    user_id: Optional[int]
    product_id: Optional[int]
    rating: Optional[int]
    comment: Optional[str]


class ReviewCreate(ReviewBase):
    pass


class ReviewOut(ReviewBase):
    
    created_at: Optional[datetime]
    user: Optional[UserInfo]  
    comment:Optional[str]
    class Config:
        from_atrribute = True 



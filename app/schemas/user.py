from pydantic import BaseModel,EmailStr
from typing import Optional
class UserBase(BaseModel):
    name:str
    email:EmailStr
class UserCreat(UserBase):
    hashed_password: str
class User(UserBase):
    id:int
    class Config:
       from_attribute = True

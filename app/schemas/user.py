from pydantic import BaseModel,EmailStr
from typing import Optional
class UserBase(BaseModel):
    name:str
    email:EmailStr
class UserCreate(UserBase):
    password: str
class Login(BaseModel):
    email:EmailStr
    password:str

class User(UserBase):
    id:int
    class Config:
       from_attribute = True

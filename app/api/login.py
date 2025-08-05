from fastapi import Depends, HTTPException, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.user import Login
from sqlalchemy.orm import Session
from app.database import get_db
from app.service.auth import authenticate_user
router=APIRouter()
@router.post("/login")
def login(form_data:Login,db:Session=Depends(get_db)):
    access_token=authenticate_user(form_data.email,form_data.hashed_password,db)
    if not access_token:
        raise HTTPException(status_code=401,detail="Invalid credentials")
    return {"access_token":access_token,"token_type":"bearer"}


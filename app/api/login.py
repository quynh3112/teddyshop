from fastapi import Depends, HTTPException, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.token import Token
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.user import Login
from app.service.auth import login_user
router=APIRouter()
@router.post("/",response_model=Token)
def login(login_data:Login,db:Session=Depends(get_db)):
    return login_user(login_data.email,login_data.password, db)
from app.crud.user import get_user_by_email
from app.core.security import verify_password,create_access_token
from sqlalchemy.orm import Session
from app.schemas.token import Token
from fastapi import HTTPException
from app.core.security import ACESS_TOKEN_EXPIRE_MINUTES
from datetime import timedelta
def authenticate_user(email:str, password:str, db:Session):
    user=get_user_by_email(email,db)
    if not user :
        return None
    if not verify_password(password,user.hashed_password):
        return None
    return user
def login_user(email: str, password: str, db: Session):
    user = authenticate_user(email, password, db)
    if not user:
        raise HTTPException(status_code=400, detail="Email hoặc mật khẩu sai")

    expire = timedelta(minutes=ACESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.email}, expires_delta=expire)
    return Token(access_token=access_token, token_type="bearer")


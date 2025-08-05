from app.crud.user import get_user_by_email
from app.core.sercurity import verify_password,create_access_token
from sqlalchemy.orm import Session
def authenticate_user(email:str,password:str,db:Session):
    user=get_user_by_email(email,db)
    if not user or verify_password(password,user.hashed_password):
        return None
    return create_access_token(data={"sub":user.email})
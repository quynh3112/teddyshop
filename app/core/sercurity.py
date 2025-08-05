from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta,timezone

pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")
SECRET_KEY="quynhteddy"
ALGORITHM="HS256"

def verify_password(plain_password,hashed_password):
    return pwd_context.verify(plain_password,hashed_password)
def create_access_token(data:dict,expires_delta:timedelta=timedelta(hours=1)):
    to_encode=data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    to_encode.update({"exp":expire})
    return jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)

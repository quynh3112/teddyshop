from sqlalchemy.orm import Session
from app.models.user import Users
from app.schemas.user import UserCreate
from app.core.security import get_password_hash

def create_user(db: Session, user: UserCreate):
    hashed_password = get_password_hash(user.password)  # password thô ở đây
    user_data = user.model_dump()
    user_data["hashed_password"] = hashed_password
    # Nếu có trường 'password' thì xóa đi vì không cần lưu raw password
    if "password" in user_data:
        del user_data["password"]
    new_user = Users(**user_data)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def update_user(db:Session, user_id:int,user_data:UserCreate):
    user=db.query(Users).filter(Users.id==user_id).first()
    if not user:
        return None
    for field , value in user_data.model_dump().items():
        setattr(user,field,value)
    db.commit()
    db.refresh(user)
    return user
def delete_user(db:Session,user_id:int):
    user=db.query(Users).filter(Users.id==user_id).first()
    if not user:
       return None
    db.delete(user)
    db.commit()
    return user
def get_all_user(db:Session):
    return db.query(Users).all()
def get_user_id(db:Session,user_id):
    user=db.query(Users).filter(Users.id==user_id).first()
    if not user:
        return None
    return user
def get_user_by_email(email:str,db:Session):
    return db.query(Users).filter(Users.email==email).first()    
    
    
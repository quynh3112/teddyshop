from sqlalchemy.orm import Session
from app.models.user import Users
from app.schemas.user import UserCreat

def create_user(db:Session,user:UserCreat):
    new_user=Users(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def update_user(db:Session, user_id:int,user_data:UserCreat):
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
    
    
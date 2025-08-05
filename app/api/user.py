from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import User, UserCreat
from app.crud import user as user_crud
from app.database import get_db
router=APIRouter()
@router.post("/", response_model=User)
def create_user(user:UserCreat, db:Session=Depends(get_db)):
    try:
        return user_crud.create_user(db, user)
    except Exception as e:
        db.rollback()
        if "Duplicate entry" in str(e):
            raise HTTPException(status_code=400, detail="Email đã tồn tại")
        raise HTTPException(status_code=400, detail="Lỗi: " + str(e))
   

@router.get("/",response_model=list[User])
def get_all_user(db:Session=Depends(get_db)):
    return user_crud.get_all_user(db)
@router.put("/{user_id}",response_model=User)
def update_user(user_id:int,user_data:UserCreat,db:Session=Depends(get_db)):
    user=user_crud.update_user(db,user_id,user_data)
    if not user:
        raise HTTPException(status_code=404,detail="Không tìm thấy người dùng")
    return user
@router.get("/{user_id}",response_model=User)
def get_user_id(user_id:int,db:Session=Depends(get_db)):
    user=user_crud.get_user_id(db,user_id)
    if not user:
        raise HTTPException(status_code=404,detail="Không tìm thấy người dùng")
    return user
@router.delete("/{user_id}",response_model=User)
def delete_user(user_id:int,db:Session=Depends(get_db)):
    user=user_crud.delete_user(db,user_id)
    if not user:
        raise HTTPException(status_code=404,detail="Không tìm thấy người dùng")
    return user
    


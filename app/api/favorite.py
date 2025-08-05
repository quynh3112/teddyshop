from sqlalchemy.orm import Session
from app.schemas.favorite import FavoriteCreate, Favourite,FavoriteOut
from app.crud import favorite as favorite_crud
from fastapi import Depends ,APIRouter,HTTPException
from app.database import get_db
router=APIRouter()
@router.post("/",response_model=Favourite)
def create_favorite(favorite:FavoriteCreate,db:Session=Depends(get_db)):
    try:
        return favorite_crud.create_favorite(db,favorite)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Lỗi:"+str(e))
@router.delete("/{favorite_id}",response_model=dict)
def delete_favorite(favorite_id:int,db:Session=Depends(get_db)):
    favorite_crud.delete_favourite(db,favorite_id)
    return {"message": "Xóa thành công"}
@router.get("/{user_id}",response_model=list[FavoriteOut])
def get_all_product_favorite_by_userid(user_id:int,db:Session=Depends(get_db)):
    return favorite_crud.get_all_favorite_with_product(user_id,db)
  
   
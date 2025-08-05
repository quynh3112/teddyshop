from sqlalchemy.orm import Session
from app.schemas.cart_item import CartItemCreate,CartItemRead
from app.crud import cart_item as cart_item_crud
from fastapi import APIRouter,Depends,HTTPException
from app.database import get_db
router=APIRouter()
@router.post("/{user_id}/{product_id}",response_model=CartItemRead)
def create_cartitem(user_id:int,product_id:int ,cartitem:CartItemCreate,db:Session=Depends(get_db)):
    try:
        return cart_item_crud.create_cart(db,cartitem,user_id,product_id)
    except Exception as e:
        raise HTTPException(status_code=404,detail="Lỗi:"+str(e))
@router.delete("/{cartitem_id}",response_model=dict)
def delete_cartitem(cartitem_id:int,db:Session=Depends(get_db)):
    try:
        cart_item_crud.delete_cart(db,cartitem_id)
        return {"message":"Xóa Thành Công"}
        
    except Exception as e:
        raise HTTPException(status_code=404,detail="Lỗi:" +str(e))
@router.get("/{user_id}",response_model=list[CartItemRead])
def get_all_cart_item_by_userid(user_id:int,db:Session=Depends(get_db)):
    return cart_item_crud.get_all_cart_items(user_id,db)
@router.put("/{user_id}/{product_id}",response_model=CartItemRead)
def decrease_item(user_id:int,product_id:int,db:Session=Depends(get_db)):
    return cart_item_crud.decrease_quantity(user_id,product_id,db)

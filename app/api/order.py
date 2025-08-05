from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends,HTTPException
from app.schemas.order import OrderCreate,Order
from app.crud import order as order_crud
from app.database import get_db


router=APIRouter()
@router.post("/",response_model=Order)
def create_order(order:OrderCreate,db:Session=Depends(get_db)):
    try:
        return order_crud.create_order(db,order)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Erro:"+str(e))

@router.get("/{user_id}",response_model=list[Order])
def get_all_order_by_userid(user_id,db:Session=Depends(get_db)):
    return order_crud.get_all_ordered_products_by_user_id(db,user_id)
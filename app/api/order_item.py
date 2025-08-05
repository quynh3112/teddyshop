from sqlalchemy.orm import Session
from fastapi import Depends,APIRouter,HTTPException
from app.schemas.oder_item  import OrderItemCreate,OrderItem
from app.crud import order_item as order_item_crud
from app.database import get_db
router=APIRouter()
@router.post("/",response_model=OrderItem)
def create_orderitem(order_item:OrderItemCreate,db:Session=Depends(get_db)):
    try:
        return order_item_crud.create_order_item(db,order_item)
    except Exception as e:
        raise HTTPException(status_code=400,detail="Lỗi:"+str(e))
@router.delete("/",response_model=dict)
def delete_orderitem(orderitem_id:int,db:Session=Depends(get_db)):
    try:
        return order_item_crud.delete_order_item(db,orderitem_id)
    except Exception as e:
        raise HTTPException(status_code=500,detail="Lỗi:"+str(e))

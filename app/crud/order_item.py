from sqlalchemy.orm import Session
from app.models.oder_items import OrderItems
from app.schemas.oder_item import OrderItemCreate



def create_order_item(db: Session, order_item: OrderItemCreate):
    new_item = OrderItems(**order_item.model_dump())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

def delete_order_item(db: Session, item_id: int):
    item = db.query(OrderItems).filter(OrderItems.id == item_id).first()
    if item:
        db.delete(item)
        db.commit()
    return item

def update_order_item(db: Session, item_id: int, updated_data: OrderItemCreate):
    item = db.query(OrderItems).filter(OrderItems.id == item_id).first()
    if item:
        for key, value in updated_data.model_dump(exclude_unset=True).items():
            setattr(item, key, value)
        db.commit()
        db.refresh(item)
    return item
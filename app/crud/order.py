from sqlalchemy.orm import Session
from app.models.order import Orders
from app.schemas.order import OrderCreate
from app.models.oder_items import OrderItems
from app.models.products import Products

def create_order(db:Session,order_data:OrderCreate):
   
    total_amount = sum(
        item.price * item.quantity for item in order_data.order_items
    )

    # Tạo đơn hàng mới
    new_order = Orders(
        user_id=order_data.user_id,
        total_amount=total_amount,
        phonenumber=order_data.phonenumber,
        address=order_data.address,
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    
    for item in order_data.order_items:
        order_item = OrderItems(
            order_id=new_order.id,
            product_id=item.product_id,
            quantity=item.quantity,
            price=item.price
        )
        db.add(order_item)

    db.commit()
    db.refresh(new_order)
    return new_order




def get_all_ordered_products_by_user_id(db: Session, user_id: int):
    return (
        db.query(OrderItems,Orders)
        .join(Orders, Orders.id == OrderItems.order_id)
        .join(Products, Products.id == OrderItems.product_id)
        .filter(Orders.user_id == user_id).first()
    )
 
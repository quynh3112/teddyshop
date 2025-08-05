from sqlalchemy.orm import Session
from app.models.cart_item import CartItems
from app.schemas.cart_item import CartItemCreate
from app.models.products import Products

def create_cart(db:Session,cart:CartItemCreate,user_id:int,product_id:int):
    cart_item=db.query(CartItems).filter(CartItems.product_id==product_id, CartItems.user_id==user_id).first()
    if cart_item:
        cart_item.quantity+=1
    else:   
        cart_item=CartItems(**cart.model_dump())
        db.add(cart_item)
    db.commit()
    db.refresh(cart_item)
    return cart_item
    
    
def delete_cart(db:Session,cart_id:int):
    cart=db.query(CartItems).filter(CartItems.id==cart_id).first()
    if not cart:
        return None
    db.delete(cart)
    db.commit()
    return cart
def get_all_cart_items(user_id,db:Session):
    return db.query(CartItems).join(Products,Products.id==CartItems.product_id).filter(CartItems.user_id==user_id).first()
def decrease_quantity(user_id:int,product_id:int,db:Session):
    cart_item=db.query(CartItems).filter(CartItems.user_id==user_id,CartItems.product_id==product_id).first()
    if cart_item.quantity > 1:
        cart_item.quantity-=1
    else:
        db.delete(cart_item)  
        db.commit()
        return {"message": "Sản phẩm đã bị xoá khỏi giỏ hàng"}
    db.commit()
    db.refresh(cart_item)
    return cart_item
   

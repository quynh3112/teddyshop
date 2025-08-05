from sqlalchemy.orm import Session
from app.models.products import Products
from app.schemas.product import ProductCreate

def create_product(db:Session,product:ProductCreate):
    new_product=Products(**product.model_dump())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

def delete_product(db:Session,product_id:int):
    product=db.query(Products).filter(Products.id==product_id).first()
    if not product:
        return None
    db.delete(product)
    db.commit()
    return product
def update_product(product_id:int,db:Session,product_data=ProductCreate):
    product=db.query(Products).filter(Products.id==product_id).first()
    if not product:
        return None
    for field, value in product_data.model_dump().items():
        setattr(product,field,value)
    db.commit()
    db.refresh(product)
    return product

def get_all_products(db:Session):
    return db.query(Products).all()

def get_product_id(db:Session,product_id:int):
    return db.query(Products).filter(Products.id==product_id).first()


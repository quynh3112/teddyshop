from sqlalchemy.orm import Session
from app.models.categories import Categories
from app.schemas.category import CategoryCreate
def create_category(db:Session,category:CategoryCreate):
    new_category=Categories(**category.model_dump())
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category
def get_all_categories(db:Session):
    return db.query(Categories).all()

def get_category_id(db:Session,category_id:int):
    return db.query(Categories).filter(Categories.id==category_id).first()

def update_cartegory(db:Session,category_id,category_data:CategoryCreate):
    category=db.query(Categories).filter(Categories.id==category_id).first()
    if not category:
        return None
    for field,value in category_data.model_dump().items():
        setattr(category,field,value)
    db.commit()
    db.refresh(category)
    return category

def delete_category(db:Session,category_id):
    category=db.query(Categories).filter(Categories.id==category_id).first()
    if not category:
        return None
    db.delete(category)
    db.commit()
    return category


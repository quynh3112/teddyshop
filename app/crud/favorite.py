from sqlalchemy.orm import Session
from app.models.favorites import Favorites
from app.schemas.favorite import FavoriteCreate
from app.models.products import Products

def create_favorite(db:Session,favorite:FavoriteCreate):
    new_favorite=Favorites(**favorite.model_dump())
    db.add(new_favorite)
    db.commit()
    db.refresh(new_favorite)
    return new_favorite

def delete_favourite(db:Session,favorite_id:int):
    favourite=db.query(Favorites).filter(Favorites.id==favorite_id).first()
    if not favourite:
        return None
    db.delete(favourite)
    db.commit()
    return favourite

def get_all_favorite_with_product(user_id: int, db: Session):
    return (
        db.query(Favorites)
        .join(Products, Favorites.product_id == Products.id)
        .filter(Favorites.user_id == user_id)
        .all()
    )


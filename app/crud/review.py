from sqlalchemy.orm import Session
from app.models.review import Reviews
from app.schemas.review import ReviewCreate
from app.models.oder_items import OrderItems
from app.models.order import Orders

def create_review(db:Session,review:ReviewCreate):
    new_review=Reviews(**review.model_dump())
    db.add(new_review)
    db.commit()
    db.refresh(new_review)
    return new_review

def update_review(db:Session,review_data:ReviewCreate,review_id):
    review=db.query(Reviews).filter(Reviews.id==review_id).first()
    if not review:
        return None
    for filed,value in review_data.model_dump().items():
        setattr(review,filed,value)
    db.commit()
    db.refresh(review)

    return review

def get_reviews_for_product(db: Session, product_id: int):
    return db.query(Reviews).filter(Reviews.product_id == product_id).all()


def delete_review(db:Session,review_id):
    review=db.query(Reviews).filter(Reviews.id==review_id)
    db.delete(review)
    db.commit()
    return review
def has_purchased(db: Session, user_id: int, product_id: int) -> bool:
    return db.query(OrderItems).join(Orders).filter(
        Orders.user_id == user_id,
        OrderItems.product_id == product_id
    ).first() is not None


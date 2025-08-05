from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud import review as review_crud
from app.database import get_db
from app.schemas.review import ReviewCreate, ReviewOut

router = APIRouter()

# ✅ Tạo review
@router.post("/", response_model=ReviewOut)
def create_review(review: ReviewCreate, db: Session = Depends(get_db)):
    if not review_crud.has_purchased(db, review.user_id, review.product_id):
        raise HTTPException(status_code=403, detail="Bạn chưa mua sản phẩm này nên không thể đánh giá.")
    return review_crud.create_review(db, review)

# ✅ Xóa review
@router.delete("/{review_id}", response_model=dict)
def delete_review(review_id: int, db: Session = Depends(get_db)):
    try:
        return review_crud.delete_review(db, review_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail="Lỗi: " + str(e))

# ✅ Lấy tất cả review theo product_id
@router.get("/ {product_id}", response_model=list[ReviewOut])
def get_reviews_for_product(product_id: int, db: Session = Depends(get_db)):
    return review_crud.get_reviews_for_product(db, product_id)
@router.put("/{review_id}",response_model=ReviewOut)
def update_review(review_id:int,review_data=ReviewCreate,db:Session=Depends(get_db)):
    return review_crud.update_review(db,review_data,review_id)











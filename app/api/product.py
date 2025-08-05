from sqlalchemy.orm import Session
from app.schemas.product import Product, ProductCreate
from app.database import get_db
from app.crud import product as product_crud
from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()

@router.post("/", response_model=Product)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    try:
        return product_crud.create_product(db, product)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="Lỗi: " + str(e))

@router.get("/", response_model=list[Product])
def get_all_products(db: Session = Depends(get_db)):
    return product_crud.get_all_products(db)

@router.get("/{product_id}", response_model=Product)
def get_product_id(product_id: int, db: Session = Depends(get_db)):
    product = product_crud.get_product_id(db,product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Không tìm thấy sản phẩm")
    return product

@router.put("/{product_id}", response_model=Product)
def update_product(product_id: int, product_data: ProductCreate, db: Session = Depends(get_db)):
    product = product_crud.update_product(product_id,db,product_data)
    if not product:
        raise HTTPException(status_code=404, detail="Không tìm thấy sản phẩm")
    return product

@router.delete("/{product_id}", response_model=dict)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = product_crud.delete_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Sản phẩm không tồn tại")
    return{"message": "Xóa sản phẩm thành công"}

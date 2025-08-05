from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.category import CategoryCreate, Category
from app.crud import category as category_crud
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=Category)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    return category_crud.create_category(db, category)

@router.get("/", response_model=list[Category])
def get_all_categories(db: Session = Depends(get_db)):
    return category_crud.get_all_categories(db)

@router.get("/{category_id}", response_model=Category)
def get_category_by_id(category_id: int, db: Session = Depends(get_db)):
    category = category_crud.get_category_id(db, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@router.put("/{category_id}", response_model=Category)
def update_category(category_id: int, category_data: CategoryCreate, db: Session = Depends(get_db)):
    category = category_crud.update_cartegory(db, category_id, category_data)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@router.delete("/{category_id}", response_model=Category)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    category = category_crud.delete_category(db, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

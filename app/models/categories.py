from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from typing import List
from ..database import Base

class Categories(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)

    products = relationship("Products", back_populates="category", passive_deletes=True)




from sqlalchemy import Column, Integer, String, Float, ForeignKey,Text
from app.database import Base
from sqlalchemy.orm import relationship

class Products(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
    description = Column(Text)
    stock_quantity = Column(Integer)
    image_url = Column(String(255))
    category_id = Column(Integer, ForeignKey("categories.id", ondelete="CASCADE"))

    category = relationship("Categories", back_populates="products", passive_deletes=True)
    order_items = relationship("OrderItems", back_populates="product", passive_deletes=True)
    cart_items = relationship("CartItems", back_populates="product", passive_deletes=True)
    favorites = relationship("Favorites", back_populates="product", passive_deletes=True)
    reviews = relationship("Reviews", back_populates="product", passive_deletes=True)


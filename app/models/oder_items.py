from sqlalchemy import Column, Integer, Float, ForeignKey,DECIMAL
from app.database import Base
from sqlalchemy.orm import relationship

class OrderItems(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id", ondelete="CASCADE"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id", ondelete="CASCADE"), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(DECIMAL(15, 0), nullable=False)  # ✅ cần thiết!

    order = relationship("Orders", back_populates="order_items", passive_deletes=True)
    product = relationship("Products", back_populates="order_items", passive_deletes=True)

from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey,func
from app.database import Base
import datetime
from sqlalchemy.orm import relationship




class Orders(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    phonenumber = Column(String(20), nullable=True)
   

    status = Column(String(50), default="pending")
    total_amount = Column(Float, nullable=True)
    address = Column(String(255), nullable=True)
    note = Column(String(255), nullable=True)

    user = relationship("Users", back_populates="orders", passive_deletes=True)
    order_items = relationship("OrderItems", back_populates="order", passive_deletes=True)

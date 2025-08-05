from sqlalchemy import Column, Integer, String, ForeignKey, Float,func,Text,DateTime
from app.database import Base
from sqlalchemy.orm import relationship
import datetime

class Reviews(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id", ondelete="CASCADE"), nullable=False)
    rating = Column(Integer)
    comment = Column(Text)
    created_at = Column(DateTime, server_default=func.now())

    user = relationship("Users", back_populates="reviews", passive_deletes=True)
    product = relationship("Products", back_populates="reviews", passive_deletes=True)




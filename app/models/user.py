from sqlalchemy import Column, Integer, String,func
from app.database import Base

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, text
from sqlalchemy.orm import relationship

import datetime

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    role = Column(String(20), default='user')
    created_at = Column(DateTime, server_default=func.now())

    orders = relationship("Orders", back_populates="user", passive_deletes=True)
    cart_items = relationship("CartItems", back_populates="user", passive_deletes=True)
    favorites = relationship("Favorites", back_populates="user", passive_deletes=True)
    reviews = relationship("Reviews", back_populates="user", passive_deletes=True)
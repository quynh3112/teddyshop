from sqlalchemy import Column, Integer, ForeignKey
from app.database import Base
from sqlalchemy.orm import relationship
class Favorites(Base):
    __tablename__ = "favorites"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id", ondelete="CASCADE"), nullable=False)

    user = relationship("Users", back_populates="favorites", passive_deletes=True)
    product = relationship("Products", back_populates="favorites", passive_deletes=True)
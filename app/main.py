


from fastapi import FastAPI
import uvicorn
from app.models.oder_items import OrderItems
from app.api import category
from app.database import engine
from app.api import user
from app.api import product
from app.api import favorite
from app.database import Base
from app.api import cart_item
from app.api import review
from app.api import order_item
from app.api import order
from app.api import login
Base.metadata.create_all(bind=engine)

app = FastAPI()


# Đăng ký router
app.include_router(category.router, prefix="/categories", tags=["Categories"])
app.include_router(user.router,prefix="/users",tags=["Users"])
app.include_router(product.router,prefix="/products",tags=["Products"])
app.include_router(favorite.router,prefix="/favorites",tags=["Favorite"])
app.include_router(review.router,prefix="/reviews",tags=["Reviews"])
app.include_router(cart_item.router,prefix="/cartitems",tags=['CartItems'])
app.include_router(order_item.router,prefix="/orderitems",tags=["OrderItems"])
app.include_router(order.router,prefix="/orders",tags=["Orders"])
app.include_router(login.router,prefix="/login")



# Chạy ứng dụng (chỉ dùng khi chạy trực tiếp)
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
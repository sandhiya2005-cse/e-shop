from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime

# Users
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    class Config:
        from_attributes = True

# Products
class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    image_url: Optional[str] = None

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int
    class Config:
        from_attributes = True

# Orders
class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int

class OrderItemResponse(BaseModel):
    id: int
    product_id: int
    quantity: int
    price_at_time: float
    class Config:
        from_attributes = True

class OrderCreate(BaseModel):
    items: List[OrderItemCreate]

class OrderResponse(BaseModel):
    id: int
    user_id: int
    total_amount: float
    status: str
    created_at: datetime
    items: List[OrderItemResponse] = []
    class Config:
        from_attributes = True

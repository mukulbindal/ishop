from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class LoginRequest(BaseModel):
    username: str
    password: str


class LoginResponse(BaseModel):
    username: str
    token: str


class User(BaseModel):
    id: int
    username: Optional[str]
    designation: Optional[str]
    password: Optional[str]


class IShopException(BaseModel):
    status: int
    message: str

# id, Name, Description, BuyPrice, Units_in_stock, SellPrice, LastUpdatedBy, LastUpdatedDate


class ProductRequest(BaseModel):
    name: str
    description: str
    buy_price: int
    units_in_stock: int
    sell_price: int


class Product(BaseModel):
    id: int
    name: str
    description: str
    buy_price: int
    units_in_stock: int
    sell_price: int
    last_updated_by: int
    last_updated_date: datetime


class ProductEditRequest(BaseModel):
    id: int
    name: Optional[str]
    description: Optional[str]
    buy_price: Optional[int]
    units_in_stock: Optional[int]
    sell_price: Optional[int]

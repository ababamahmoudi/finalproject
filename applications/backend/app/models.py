from sqlalchemy import Column, Integer, String, Float
from .db import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Float)
    stock = Column(Integer, default=0)

    sku = Column(String, unique=True, index=True, nullable=False)
    category = Column(String, nullable=True)


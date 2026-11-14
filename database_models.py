from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()

class Product(base):

    __tablename__ = "product"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(String(100))
    price = Column(Float)
    quantite = Column(Integer)
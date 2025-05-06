# app/models.py
from sqlalchemy import Column, Integer, String, Float, Date
from .database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(String)  # Could also use Date, but we'll keep it simple for now
    description = Column(String)
    amount = Column(Float)
    category = Column(String, default="Uncategorized")

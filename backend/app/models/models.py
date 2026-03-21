from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, timezone
from app.database import Base
from sqlalchemy.sql import func

class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    phone = Column(String, nullable=True)
    status = Column(String, default="lead") 
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
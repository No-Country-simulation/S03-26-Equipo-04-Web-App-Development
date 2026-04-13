from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.sql import func
from app.database import Base

class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    phone = Column(String, nullable=True)
    
    # Nuevos campos para el CRM
    status = Column(String, default="active") 
    funnel_stage = Column(String, default="lead") 
    tags = Column(String, nullable=True) 
    notes = Column(Text, nullable=True) 
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
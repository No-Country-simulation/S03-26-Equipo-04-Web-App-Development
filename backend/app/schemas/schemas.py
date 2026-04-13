from pydantic import BaseModel, EmailStr
from typing import Optional

class ContactBase(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None
    status: Optional[str] = "active"
    funnel_stage: Optional[str] = "lead"
    tags: Optional[str] = None
    notes: Optional[str] = None

class ContactCreate(ContactBase):
    pass

class ContactUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    status: Optional[str] = None
    funnel_stage: Optional[str] = None
    tags: Optional[str] = None
    notes: Optional[str] = None

class ContactResponse(ContactBase):
    id: int
    
    class Config:
        from_attributes = True
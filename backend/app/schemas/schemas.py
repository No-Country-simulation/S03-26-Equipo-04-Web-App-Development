from pydantic import BaseModel, EmailStr
from typing import Optional

# Esquema base con los campos comunes para un contacto
class ContactBase(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None
    status: Optional[str] = "lead"

# Esquema para la creación de nuevos contactos. No requiere ID
class ContactCreate(ContactBase):
    pass

# Esquema de respuesta que incluye el ID generado por la base de datos
class ContactResponse(ContactBase):
    id: int
    
    class Config:
        from_attributes = True
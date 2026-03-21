from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.models import Contact
from app.schemas.schemas import ContactCreate, ContactResponse

router = APIRouter(prefix="/contacts", tags=["Contacts"])

@router.post("/", response_model=ContactResponse, status_code=201)
def create_contact(contact: ContactCreate, db: Session = Depends(get_db)):
    db_contact = Contact(
        name=contact.name,
        email=contact.email,
        phone=contact.phone,
        status=contact.status
    )
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact

@router.get("/", response_model=List[ContactResponse])
def get_all_contacts(db: Session = Depends(get_db)):
    return db.query(Contact).all()


@router.get("/{contact_id}", response_model=ContactResponse)
def get_contact_by_id(contact_id: int, db: Session = Depends(get_db)):
    db_contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if not db_contact:
        raise HTTPException(status_code=404, detail="Contacto no encontrado")
    return db_contact
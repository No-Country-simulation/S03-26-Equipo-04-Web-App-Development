from fastapi import FastAPI
from app.database import engine, Base
from app.routers import contacts, mocks # Importamos los nuevos archivos

# Creamos las tablas en PostgreSQL
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="🧩 Startup CRM API",
    description="API para gestión de leads y clientes con integración de canales",
    version="1.0.0"
)

# Incluimos las rutas de los archivos externos
app.include_router(contacts.router)
app.include_router(mocks.router)

@app.get("/")
def read_root():
    return {"message": "Startup CRM API is running 🚀", "docs": "/docs"}
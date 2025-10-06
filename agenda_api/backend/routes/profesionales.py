from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas import ProfesionalCreate
from crud.profesionales import crear_profesional, listar_profesionales
router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/profesionales/")
def registrar_profesional(profesional: ProfesionalCreate, db: Session = Depends(get_db)):
    return crear_profesional(db, profesional)

@router.get("/profesionales/")
def obtener_usuarios(db: Session = Depends(get_db)):
    return listar_profesionales(db)


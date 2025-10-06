from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas import ProfesionCreate
from crud.profesion import crear_profesion, listar_profesion

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/profesion/")
def registrar_profesion(profesion: ProfesionCreate, db: Session = Depends(get_db)):
    return crear_profesion(db, profesion)

@router.get("/profesion/")
def obtener_profesiones(db: Session = Depends(get_db)):
    return listar_profesion(db)

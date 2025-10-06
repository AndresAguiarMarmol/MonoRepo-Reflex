from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas import CitaCreate
from crud.citas import crear_cita, listar_citas
router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/citas/")
def registrar_cita(cita: CitaCreate, db: Session = Depends(get_db)):
    return crear_cita(db, cita)

@router.get("/citas/")
def obtener_usuarios(db: Session = Depends(get_db)):
    return listar_citas(db)


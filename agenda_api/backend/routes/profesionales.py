from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from crud import profesionales as crud
from schemas import Profesional, ProfesionalCreate
from typing import List

router = APIRouter(prefix="/profesionales", tags=["Profesionales"])

@router.post("/", response_model=Profesional)
def crear(datos: ProfesionalCreate, db: Session = Depends(get_db)):
    return crud.crear_profesional(db, datos)

@router.get("/", response_model=List[Profesional])
def listar(db: Session = Depends(get_db)):
    return crud.listar_profesionales(db)






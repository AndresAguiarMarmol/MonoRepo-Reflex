from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from crud import profesiones as crud
from schemas import Profesiones, ProfesionCreate
from typing import List

router = APIRouter(prefix="/profesiones", tags=["Profesiones"])

@router.post("/", response_model=Profesiones)
def crear(datos: ProfesionesCreate, db: Session = Depends(get_db)):
    return crud.crear_profesiones(db, datos)

@router.get("/", response_model=List[Profesiones])
def listar(db: Session = Depends(get_db)):
    return crud.listar_profesiones(db)

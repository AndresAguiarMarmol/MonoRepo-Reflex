from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from crud import citas as crud
from schemas import citas, CitaCreate
from typing import List

router = APIRouter(prefix="/citas", tags=["Citas"])

@router.post("/", response_model=Citas)
def crear(datos: CitasCreate, db: Session = Depends(get_db)):
    return crud.crear_cita(db, datos)

@router.get("/", response_model=List[Citas])
def listar(db: Session = Depends(get_db)):
    return crud.listar_citas(db)




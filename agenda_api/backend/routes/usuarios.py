from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from crud import usuarios as crud
from schemas import Usuarios, UsuarioCreate
from typing import List

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.post("/", response_model=Usuarios)
def crear(datos: UsuariosCreate, db: Session = Depends(get_db)):
    return crud.crear_usuarios(db, datos)

@router.get("/", response_model=List[Usuarios])
def listar(db: Session = Depends(get_db)):
    return crud.listar_usuarios(db)



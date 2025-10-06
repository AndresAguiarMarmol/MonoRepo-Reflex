from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas import UsuarioCreate
from crud.usuarios import crear_usuario, listar_usuarios

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/usuarios/")
def registrar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    return crear_usuario(db, usuario)

@router.get("/usuarios/")
def obtener_usuarios(db: Session = Depends(get_db)):
    return listar_usuarios(db)


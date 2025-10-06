from sqlalchemy.orm import Session
from models import Usuario
from schemas import UsuarioCreate

def crear_usuario(db: Session, datos: UsuarioCreate):
    usuario = Usuario(**datos.dict())
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return usuario

def listar_usuarios(db: Session):
    return db.query(Usuario).all()





from sqlalchemy.orm import Session
from models import Profesional
from schemas import ProfesionalCreate

def crear_profesional(db: Session, datos: ProfesionalCreate):
    nuevo = Profesional(**datos.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def listar_profesionales(db: Session):
    return db.query(Profesional).all()






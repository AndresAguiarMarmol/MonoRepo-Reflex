
from sqlalchemy.orm import Session
from models import Cita
from schemas import CitaCreate

def crear_cita(db: Session, datos: CitaCreate):
    nueva = Cita(**datos.dict())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

def listar_citas(db: Session):
    return db.query(Cita).all()


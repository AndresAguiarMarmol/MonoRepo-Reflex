from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from database import Base
from sqlalchemy.orm import Session
from models import Cita
from models import Profesional
from models import Profesion
from models import Usuario
from schemas import CitaCreate
from schemas import ProfesionCreate
from schemas import ProfesionalCreate
from schemas import UsuarioCreate


class UsuarioCreate(BaseModel):
    id :int
    nombre = str
    email = str
    telefono: str
    correo: str

class ProfesionalCreate(BaseModel):
    nombre: str
    profesion_id: int

class ProfesionCreate(BaseModel):
    nombre: str

class CitaCreate(BaseModel):
    usuario_id: int
    profesional_id: int
    fecha: str
    hora: str
    lugar: str
    descripcion: str

class Profesional(Base):
    __tablename__ = "profesionales"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    especialidad = Column(String, nullable=False)
    telefono = Column(String, nullable=True)

class Citas(Base):  #Revisar Definicion de Tabla
    __tablename__ = "citas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    especialidad = Column(String, nullable=False)
    telefono = Column(String, nullable=True)

class Profesion(Base):  #Revisar Definicion de Tabla
    __tablename__ = "profesion"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    especialidad = Column(String, nullable=False)
    telefono = Column(String, nullable=True)

class Usuario(Base):  #Revisar Definicion de Tabla
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    especialidad = Column(String, nullable=False)
    telefono = Column(String, nullable=True)

def crear_cita(db: Session, datos: CitaCreate):
    nueva = Cita(**datos.dict())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

def listar_citas(db: Session):
    return db.query(Cita).all()

def crear_profesional(db: Session, datos: ProfesionalCreate):
    nueva = Profesional(**datos.dict())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

def listar_Profesionales(db: Session):
    return db.query(listar_Profesionales).all()

def crear_profesion(db: Session, datos: ProfesionCreate):
    nueva = Profesion(**datos.dict())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

def listar_Profesion(db: Session):
    return db.query(listar_Profesion).all()

def crear_usuarios(db: Session, datos: UsuarioCreate):
    nueva = Usuario(**datos.dict())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

def listar_Usuarios(db: Session):
    return db.query(listar_Usuarios).all()

    
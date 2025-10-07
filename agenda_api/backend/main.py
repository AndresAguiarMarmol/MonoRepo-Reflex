
# main.py
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Text, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from routes import profesionales
app.include_router(profesionales.router)

# Configuración de base de datos
DATABASE_URL = "sqlite:///./medicapp.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

# Modelos SQLAlchemy
class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    telefono = Column(String, unique=True)
    correo = Column(String, unique=True)

class Citas(Base):
    __tablename__ = "citas"
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    fecha = Column(String)
    hora = Column(String)
    lugar = Column(String)
    descripcion = Column(Text)

class Profesiones(Base):
    __tablename__ = "Profesiones"
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    fecha = Column(String)
    hora = Column(String)
    lugar = Column(String)
    descripcion = Column(Text)

Base.metadata.create_all(bind=engine)

# Modelos Pydantic
class UsuarioCreate(BaseModel):
    nombre: str
    telefono: str
    correo: str

class CitaCreate(BaseModel):
    usuario_id: int
    fecha: str
    hora: str
    lugar: str
    descripcion: str

# Inicializar FastAPI
app = FastAPI()

# Dependencia para obtener sesión DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




from fastapi import FastAPI
from database import Base, engine
from routes import usuarios, profesionales, profesiones, citas

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(usuarios.router)
app.include_router(profesionales.router)
app.include_router(profesiones.router)
app.include_router(citas.router)
from routes import profesionales
from routes import profesiones
from routes import citas
from routes import usuarios





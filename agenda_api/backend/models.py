
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

class Profesion(Base):
    __tablename__ = "profesiones"
    id = Column(Integer, primary_key=True)
    nombre = Column(String, unique=True)

from sqlalchemy import Column, Integer, String

class Profesional(Base):
    __tablename__ = "profesionales"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    especialidad = Column(String, nullable=False)
    telefono = Column(String, nullable=True)

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    telefono = Column(String, unique=True)
    correo = Column(String, unique=True)

class Cita(Base):
    __tablename__ = "citas"

    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(DateTime, nullable=False)
    motivo = Column(String, nullable=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    profesional_id = Column(Integer, ForeignKey("profesionales.id"))
    usuario = relationship("Usuario")
    profesional = relationship("Profesional")







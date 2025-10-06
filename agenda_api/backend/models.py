
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Profesion(Base):
    __tablename__ = "profesiones"
    id = Column(Integer, primary_key=True)
    nombre = Column(String, unique=True)

class Profesional(Base):
    __tablename__ = "profesionales"
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    profesion_id = Column(Integer, ForeignKey("profesiones.id"))
    profesion = relationship("Profesion")

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    telefono = Column(String, unique=True)
    correo = Column(String, unique=True)

class Cita(Base):
    __tablename__ = "citas"
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    profesional_id = Column(Integer, ForeignKey("profesionales.id"))
    fecha = Column(String)
    hora = Column(String)
    lugar = Column(String)
    descripcion = Column(Text)


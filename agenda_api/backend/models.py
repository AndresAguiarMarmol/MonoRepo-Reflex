from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

class Cita(Base):
    __tablename__ = "citas"

    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(DateTime, nullable=False)
    motivo = Column(String, nullable=True)

    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    profesional_id = Column(Integer, ForeignKey("profesionales.id"))

    usuario = relationship("Usuario")
    profesional = relationship("Profesional")

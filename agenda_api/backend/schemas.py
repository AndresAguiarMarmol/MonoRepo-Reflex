from pydantic import BaseModel
from datetime import datetime

class CitaBase(BaseModel):
    fecha: datetime
    motivo: str | None = None
    usuario_id: int
    profesional_id: int

class CitaCreate(CitaBase):
    pass

class Cita(CitaBase):
    id: int

    class Config:
        orm_mode = True

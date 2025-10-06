from pydantic import BaseModel

class UsuarioCreate(BaseModel):
    nombre: str
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
    
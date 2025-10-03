
# frontend/state/registro_state.py

import reflex as rx
from backend.auth import insertar_usuario

class RegistroState(rx.State):
    rut: str = ""
    nombre: str = ""
    apellido: str = ""
    telefono: str = ""
    email: str = ""
    password: str = ""
    rol: str = "paciente"
    mensaje: str = ""

    def registrar_usuario(self):
        if self.rut and self.nombre and self.apellido and self.email :
            exito = insertar_usuario(self.nombre, self.rut, self.telefono, self.email, self.password, self.rol, self.apellido)
            if exito:
                self.mensaje = "✅ Usuario registrado correctamente"
                self.rut = ""
                self.nombre = ""
                self.apellido = ""
                self.telefono = ""
                self.email = ""
                self.password = ""
                self.rol = ""
            else:
                self.mensaje = "⚠️ El correo ya está registrado"
        else:
            self.mensaje = "⚠️ Todos los campos son obligatorios"



# frontend/state/registro_state.py

import reflex as rx
from backend.auth import insertar_usuario

class RegistroState(rx.State):
    nombre: str = ""
    email: str = ""
    password: str = ""
    mensaje: str = ""

    def registrar_usuario(self):
        if self.nombre and self.email and self.password:
            exito = insertar_usuario(self.nombre, self.email, self.password)
            if exito:
                self.mensaje = "✅ Usuario registrado correctamente"
                self.nombre = ""
                self.email = ""
                self.password = ""
            else:
                self.mensaje = "⚠️ El correo ya está registrado"
        else:
            self.mensaje = "⚠️ Todos los campos son obligatorios"

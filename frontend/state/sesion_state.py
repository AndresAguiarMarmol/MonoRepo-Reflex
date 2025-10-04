# frontend/state/sesion_state.py

import reflex as rx
from backend.bd import crear_usuario, validar_login

class SesionState(rx.State):
    email: str = ""
    password: str = ""
    mensaje: str = ""
    sesion_activa: bool = False
    usuario_id: int = 0
    rol: str = ""

    def login(self):
        try:
            resultado = validar_login(self.email, self.password)
            if resultado:
                self.sesion_activa = True
                self.usuario_id = resultado["id"]
                self.rol = resultado["rol"]
                self.mensaje = "✅ Sesión iniciada"
                rx.redirect("/dashboard")
            else:
                self.mensaje = "⚠️ Credenciales incorrectas"
        except Exception as e:
            self.mensaje = "⚠️ Error en el proceso de inicio de sesión: " + str(e)


    def logout(self):
        self.sesion_activa = False
        self.usuario_id = 0
        self.rol = ""
        self.email = ""
        self.password = ""
        self.mensaje = ""
        rx.redirect("/login")

    def registrar(self, nombre: str):
        if self.email and self.password:
            exito = crear_usuario(nombre, self.email, self.password)
            self.mensaje = "✅ Registro exitoso" if exito else "⚠️ El correo ya existe"
        else:
            self.mensaje = "⚠️ Todos los campos son obligatorios"

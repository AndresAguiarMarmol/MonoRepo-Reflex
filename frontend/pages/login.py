# frontend/pages/login.py

import reflex as rx
from frontend.state.sesion_state import SesionState

def login():
    return rx.center(
        rx.vstack(
            rx.heading("Iniciar Sesión"),
            rx.input("Email", on_change=SesionState.set_email, value=SesionState.email),
            rx.input("Contraseña", type_="password", on_change=SesionState.set_password, value=SesionState.password),
            rx.button("Entrar", on_click=SesionState.login),
            rx.text(SesionState.mensaje, color="red"),
            spacing="4", max_width="400px"
        ),
        height="5"
    )

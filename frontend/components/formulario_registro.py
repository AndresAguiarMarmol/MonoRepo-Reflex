
# frontend/components/formulario_registro.py

import reflex as rx
from frontend.state.registro_state import RegistroState


def formulario_registro():
    return rx.vstack(
        rx.heading("Registro de Usuario", size="5"),
        rx.input(
            placeholder="Nombre",
            on_change=RegistroState.set_nombre,
            value=RegistroState.nombre
        ),
        rx.input(
            placeholder="Email",
            on_change=RegistroState.set_email,
            value=RegistroState.email
        ),
        rx.input(
            placeholder="Contraseña",
            type_="password",
            on_change=RegistroState.set_password,
            value=RegistroState.password
        ),
        rx.button("Registrar", on_click=RegistroState.registrar_usuario),
        rx.text(RegistroState.mensaje, color="red"),
        spacing="4",
        width="100%",
        max_width="400px"
    )

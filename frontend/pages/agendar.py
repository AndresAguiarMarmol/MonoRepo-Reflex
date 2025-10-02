# frontend/pages/agendar.py

import reflex as rx
from frontend.components.formulario_cita import formulario_cita

def agendar():
    return rx.center(
        formulario_cita(),
        height="8"
    )

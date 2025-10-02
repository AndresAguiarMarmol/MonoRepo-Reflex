
# frontend/pages/registro.py

import reflex as rx
from frontend.components.formulario_registro import formulario_registro

def registro():
    return rx.center(
        formulario_registro(),
        height="5"
    )



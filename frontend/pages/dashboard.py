# frontend/pages/dashboard.py

import reflex as rx
from frontend.state.sesion_state import SesionState

def dashboard():
    return rx.cond(
        SesionState.sesion_activa,
        rx.text(f"Bienvenido, usuario {SesionState.usuario_id}"),
        rx.script("window.location.href = '/login';")  # ✅ Redirección válida
)

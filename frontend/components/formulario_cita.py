# frontend/components/formulario_cita.py

import reflex as rx
from frontend.state.cita_state import CitaState

def formulario_cita():
    """
    return rx.vstack(
#        rx.heading("Agendar Cita", size="5"),
#        rx.input("ID del paciente", on_change=CitaState.set_paciente_id, value=CitaState.paciente_id),
#        rx.input("ID del médico", on_change=CitaState.set_medico_id, value=CitaState.medico_id),
#        rx.input("Fecha (YYYY-MM-DD)", on_change=CitaState.set_fecha, value=CitaState.fecha),
#        rx.input("Hora (HH:MM)", on_change=CitaState.set_hora, value=CitaState.hora),
        rx.text_area("Motivo", on_change=CitaState.set_motivo, value=CitaState.motivo),
#        rx.button("Agendar", on_click=CitaState.agendar),
#        rx.text(CitaState.mensaje, color="red"),
#        spacing="4",
#        width="100%",
#        max_width="400px"
    )

"""
    return rx.vstack(
        rx.heading("Agendar Cita", size="5"),
        rx.input(
            placeholder="ID del Paciente",
            on_change=CitaState.set_paciente_id,
            value=CitaState.paciente_id
        ),
        rx.input(
            placeholder="ID del médico",
            on_change=CitaState.set_medico_id,
            value= CitaState.medico_id
        ),
        rx.input(
            placeholder="Fecha (YYYY-MM-DD)",
            on_change=CitaState.set_fecha,
            value=CitaState.fecha
        ),
        rx.input(
            placeholder="Hora (HH:MM)",
            on_change=CitaState.set_hora,
            value=CitaState.hora
        ),
        rx.input(
            placeholder="Motivo",
            on_change=CitaState.set_motivo,
            value=CitaState.motivo
        ),
        rx.button("Agendar", on_click=CitaState.agendar),
        rx.text(CitaState.mensaje, color="red"),
        spacing="4",
        width="100%",
        max_width="400px"
    )
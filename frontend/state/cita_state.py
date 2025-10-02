# frontend/state/cita_state.py

import reflex as rx
from backend.citas import insertar_cita

class CitaState(rx.State):
    paciente_id: str = ""
    medico_id: str = ""
    fecha: str = ""
    hora: str = ""
    motivo: str = ""
    mensaje: str = ""

    def agendar(self):
        if self.paciente_id and self.medico_id and self.fecha and self.hora:
            exito = insertar_cita(
                int(self.paciente_id),
                int(self.medico_id),
                self.fecha,
                self.hora,
                self.motivo
            )
            self.mensaje = "✅ Cita agendada correctamente" if exito else "⚠️ Error al agendar cita"
        else:
            self.mensaje = "⚠️ Todos los campos son obligatorios"

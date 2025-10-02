import sqlite3

def insertar_cita(paciente_id, medico_id, fecha, hora, motivo=""):
    conn = sqlite3.connect("agenda.db")
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO citas (paciente_id, medico_id, fecha, hora, motivo)
            VALUES (?, ?, ?, ?, ?)
        """, (paciente_id, medico_id, fecha, hora, motivo))
        conn.commit()
        return True
    except Exception as e:
        print("Error al insertar cita:", e)
        return False
    finally:
        conn.close()
from backend.bd import get_connection
from backend.models.appointment import Appointment

def create_appointment(app: Appointment):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO appointments (user_id, date, time, reason) VALUES (?, ?, ?, ?)", 
                   (app.user_id, app.date, app.time, app.reason))
    conn.commit()

def get_appointment_by_id(app_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM appointments WHERE id = ?", (app_id,))
    return cursor.fetchone()

def update_appointment(app_id: int, updated_app: Appointment):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE appointments SET user_id = ?, date = ?, time = ?, reason = ? WHERE id = ?", 
                   (updated_app.user_id, updated_app.date, updated_app.time, updated_app.reason, app_id))
    conn.commit()

def delete_appointment(app_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM appointments WHERE id = ?", (app_id,))
    conn.commit()

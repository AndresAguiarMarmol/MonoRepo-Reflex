import sqlite3

def insertar_usuario(nombre, email, password, rol="paciente"):
    conn = sqlite3.connect("agenda.db")
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO usuarios (nombre, email, password, rol)
            VALUES (?, ?, ?, ?)
        """, (nombre, email, password, rol))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        # Email duplicado o error de restricción
        return False
    finally:
        conn.close()

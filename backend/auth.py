import sqlite3

def insertar_usuario(nombre, rut, telefono, email, password, rol, apellido):
    conn = sqlite3.connect("basedatos.db")
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO pacientes (nombre, rut, telefono, correo, password, rol, apellido)
            VALUES (?, ?, ?, ?, ? ,?, ?)
        """, ( nombre, rut, telefono, email, password, rol, apellido))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        # Email duplicado o error de restricción
        return False
    finally:
        conn.close()

# backend/db.py

import sqlite3

DB_NAME = "basedatos.db"

def conectar():
    return sqlite3.connect(DB_NAME)

import sqlite3

def crear_tablas():
    conn = conectar()
    conn = sqlite3.connect("basedatos.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pacientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        rut TEXT UNIQUE NOT NULL,
        telefono TEXT,
        correo TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS medicos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        especialidad TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS citas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        paciente_id INTEGER NOT NULL,
        medico_id INTEGER NOT NULL,
        fecha TEXT NOT NULL,
        hora TEXT NOT NULL,
        motivo TEXT,
        FOREIGN KEY (paciente_id) REFERENCES pacientes(id),
        FOREIGN KEY (medico_id) REFERENCES medicos(id)
    )
    """)

def crear_usuario(nombre, email, password, rol="paciente"):
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


def registrar_paciente(nombre, rut, telefono, correo):
        conn = sqlite3.connect("basedatos.db")
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO pacientes (nombre, rut, telefono, correo)
        VALUES (?, ?, ?, ?)
        """, (nombre, rut, telefono, correo))


def obtener_id_paciente_por_rut(rut):
    conn = sqlite3.connect("basedatos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM pacientes WHERE rut = ?", (rut,))
    resultado = cursor.fetchone()
    conn.close()
    return resultado[0] if resultado else None

def registrar_cita(rut_paciente, id_medico, fecha, hora, motivo):
    paciente_id = obtener_id_paciente_por_rut(rut_paciente)
    if paciente_id is None:
        print("Paciente no encontrado.")
        return

    conn = sqlite3.connect("basedatos.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO citas (paciente_id, medico_id, fecha, hora, motivo)
        VALUES (?, ?, ?, ?, ?)
    """, (paciente_id, id_medico, fecha, hora, motivo))

def validar_login(email, password):
    conn = sqlite3.connect("agenda.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, rol FROM usuarios WHERE email = ? AND password = ?
    """, (email, password))
    resultado = cursor.fetchone()
    conn.close()
    if resultado:
        return {"id": resultado[0], "rol": resultado[1]}
    return None


    conn.commit()
    conn.close()

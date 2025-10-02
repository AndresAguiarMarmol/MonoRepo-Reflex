# backend/db.py

import sqlite3

DB_NAME = "agenda.db"

def conectar():
    return sqlite3.connect(DB_NAME)

def crear_tablas():
    conn = conectar()
    cursor = conn.cursor()

    # Tabla usuarios
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        rol TEXT NOT NULL,
        activo INTEGER DEFAULT 1
    )
    """)

    # Tabla citas
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS citas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        paciente_id INTEGER NOT NULL,
        medico_id INTEGER NOT NULL,
        fecha TEXT NOT NULL,
        hora TEXT NOT NULL,
        motivo TEXT,
        estado TEXT DEFAULT 'pendiente',
        FOREIGN KEY(paciente_id) REFERENCES usuarios(id),
        FOREIGN KEY(medico_id) REFERENCES usuarios(id)
    )
    """)

    conn.commit()
    
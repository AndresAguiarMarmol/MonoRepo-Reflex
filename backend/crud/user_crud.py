from backend.bd import get_connection
from backend.crud.appointment_crud import User

def create_user(user: User):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email, role) VALUES (?, ?, ?)", 
                   (user.name, user.email, user.role))
    conn.commit()

def get_user_by_id(user_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()

def update_user(user_id: int, updated_user: User):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET name = ?, email = ?, role = ? WHERE id = ?", 
                   (updated_user.name, updated_user.email, updated_user.role, user_id))
    conn.commit()

def delete_user(user_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()

import uuid
from db import get_db_connection

# Check if a session exists in the database
def get_session_from_db(session_id: str):
    """Fetch session data from the database"""
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM sessions WHERE session_id = %s", (session_id,))
    session = cursor.fetchone()
    cursor.close()
    conn.close()
    return session


# Create a new session in the database
def create_session(user_id: int) -> str:
    """Create a new session for the user"""
    session_id = str(uuid.uuid4().hex)
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO sessions (session_id, user_id, created_at) VALUES (%s, %s, NOW())",
        (session_id, user_id),
    )
    conn.commit()
    cursor.close()
    conn.close()
    return session_id

def delete_session(session_id: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM sessions WHERE session_id = %s", (session_id,))
    conn.commit()
    cursor.close()
    conn.close()
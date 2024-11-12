from db import get_db_connection
import utils

# Create a new user (for testing purposes)
def create_user(username: str, password: str):
    """Create a new user in the database (hash password)"""
    hashed_password = utils.hash_password(password)
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (username, password) VALUES (%s, %s)",
        (username, hashed_password),
    )
    conn.commit()
    cursor.close()
    conn.close()


# Get user from database by username
def get_user_by_username(username: str):
    """Fetch user data from the database"""
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)  # Use dictionary=True to get results as a dict
    query = "SELECT id, username, email, password FROM users WHERE username = %s"
    cursor.execute(query, (username,))
    user = cursor.fetchone()  # Fetch the first matching row

    cursor.close()
    conn.close()
    return user



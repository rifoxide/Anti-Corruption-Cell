import os
import mysql.connector

# Database configuration
DB_CONFIG = {
    "host": os.getenv("DATABASE_HOST"),
    "user": os.getenv("DATABASE_USER"),
    "password": os.getenv("DATABASE_PASSWORD"),
    "database": os.getenv("DATABASE_NAME"),
}


def get_db_connection():
    """Establish and return a MySQL connection"""
    return mysql.connector.connect(
        **DB_CONFIG, charset="utf8mb4", collation="utf8mb4_unicode_ci"
    )

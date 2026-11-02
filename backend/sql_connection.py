"""MySQL connection shared by the DAOs. Credentials come from environment variables (see .env.example)."""

import os

import mysql.connector

__cnx = None


def get_sql_connection():
    global __cnx
    if __cnx is None:
        __cnx = mysql.connector.connect(
            user=os.environ.get("DB_USER", "root"),
            password=os.environ.get("DB_PASSWORD", ""),
            host=os.environ.get("DB_HOST", "127.0.0.1"),
            database=os.environ.get("DB_NAME", "grocery_store"),
        )
    return __cnx

import sqlite3

DB_NAME = "treasure_hunt.db"

def get_connect():
    return sqlite3.connect(DB_NAME)
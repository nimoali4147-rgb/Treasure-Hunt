import sqlite3


DB_NAME = "treasure_hunt.db"


def get_connect():
    return sqlite3.connect(DB_NAME)


def create_player_table():

    db = get_connect()
    data = db.cursor()

    data.execute("""
        CREATE TABLE IF NOT EXISTS player (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            score INTEGER DEFAULT 0
        )
    """)

    db.commit()
    db.close()
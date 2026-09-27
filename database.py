import sqlite3


DB_NAME = "treasure_hunt.db"


def get_connect():
    return sqlite3.connect(DB_NAME)


def create_tables():

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

    data.execute("""
        CREATE TABLE IF NOT EXISTS locations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )
    """)

    data.execute("""
        CREATE TABLE IF NOT EXISTS treasures (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            points INTEGER NOT NULL
        )
    """)

    data.execute("""
        CREATE TABLE IF NOT EXISTS collections (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player_id INTEGER,
            treasure_id INTEGER,
            FOREIGN KEY (player_id) REFERENCES player(id),
            FOREIGN KEY (treasure_id) REFERENCES treasures(id)
        )
    """)

    data.execute("""
        CREATE TABLE IF NOT EXISTS game_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player_id INTEGER,
            player_name TEXT,
            location TEXT,
            points INTEGER,
            result TEXT,
            FOREIGN KEY (player_id) REFERENCES player(id)
        )
    """)

    db.commit()
    db.close()


def add_locations():

    db = get_connect()
    data = db.cursor()

    locations = [
        "Forest",
        "Cave",
        "Island",
        "Desert"
    ]

    for location in locations:

        data.execute(
            "INSERT OR IGNORE INTO locations (name) VALUES (?)",
            (location,)
        )

    db.commit()
    db.close()


def add_treasures():

    db = get_connect()
    data = db.cursor()

    treasures = [
        ("Golden Coin", 100),
        ("Silver Coin", 50),
        ("Diamond", 250),
        ("Ancient Necklace", 150),
        ("Ruby", 200),
        ("Empty Chest", 0)
    ]

    for treasure in treasures:

        data.execute("""
            INSERT INTO treasures (name, points)
            SELECT ?, ? 
            WHERE NOT EXISTS (
                SELECT 1
                FROM treasures
                WHERE name = ?
            )
            """, (
                treasure[0],
                treasure[1],
                treasure[0],
            )
            
        )

    db.commit()
    db.close()
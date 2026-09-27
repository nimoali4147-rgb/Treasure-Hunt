import random
from database import get_connect


def find_treasure():

    db = get_connect()
    data = db.cursor()

    data.execute("""
        SELECT id, name, points
        FROM treasures
    """)

    treasures = data.fetchall()

    db.close()

    treasure = random.choice(treasures)

    return treasure
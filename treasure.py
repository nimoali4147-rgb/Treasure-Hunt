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


def save_treasure(player_id, treasure_id):

    db = get_connect()
    data = db.cursor()

    data.execute("""
        INSERT INTO collections (player_id, treasure_id)
        VALUES (?, ?)
    """, (player_id, treasure_id))

    db.commit()
    db.close()


def update_score(player_id, points):

    db = get_connect()
    data = db.cursor()

    data.execute("""
        UPDATE player
        SET score = score + ?
        WHERE id = ?
    """, (points, player_id))

    db.commit()
    db.close()


def get_score(player_id):

    db = get_connect()
    data = db.cursor()

    data.execute("""
        SELECT score
        FROM player
        WHERE id = ?
    """, (player_id,))

    score = data.fetchone()

    db.close()

    return score[0]
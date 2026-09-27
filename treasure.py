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


def show_treasures(player_id):
    db = get_connect()
    data = db.cursor()

    data.execute("""
        SELECT treasures.name, treasures.points
        FROM collections
        JOIN treasures
        ON collections.treasure_id = treasures.id
        WHERE collections.player_id = ?
    """, (player_id,))

    treasures = data.fetchall()

    db.close()

    print("\nMY TREASURES")

    if not treasures:
        print("You have not found any treasures yet.")
        return

    for treasure in treasures:
        print(treasure[0], "-", treasure[1], "points")


def save_history(player_id, player_name, location, points, result):
    db = get_connect()
    data = db.cursor()

    data.execute("""
        INSERT INTO game_history (
            player_id,
            player_name,
            location,
            points,
            result
        )
        VALUES (?, ?, ?, ?, ?)
    """, (
        player_id,
        player_name,
        location,
        points,
        result
    ))

    db.commit()
    db.close()

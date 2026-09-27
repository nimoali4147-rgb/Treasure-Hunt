from flask import Flask, request
from flask import Flask
from database import get_connect

app = Flask(__name__)


@app.route("/")
def home():
    return {
        "message": "Treasure Hunt API is running"
    }


@app.route("/players", methods=["GET"])
def get_players():
    db = get_connect()
    data = db.cursor()

    data.execute("""
        SELECT id, first_name, last_name, score
        FROM player
    """)

    players = data.fetchall()

    db.close()

    result = []

    for player in players:
        result.append({
            "id": player[0],
            "first_name": player[1],
            "last_name": player[2],
            "score": player[3]
        })

    return result


@app.route("/players/<int:player_id>", methods=["GET"])
def get_player(player_id):
    db = get_connect()
    data = db.cursor()

    data.execute("""
        SELECT id, first_name, last_name, score
        FROM player
        WHERE id = ?
    """, (player_id,))

    player = data.fetchone()

    db.close()

    if player is None:
        return {
            "message": "Player not found"
        }, 404

    return {
        "id": player[0],
        "first_name": player[1],
        "last_name": player[2],
        "score": player[3]
    }


@app.route("/treasures", methods=["GET"])
def get_treasures():
    db = get_connect()
    data = db.cursor()

    data.execute("""
        SELECT id, name, points
        FROM treasures
    """)

    treasures = data.fetchall()

    db.close()

    result = []

    for treasure in treasures:
        result.append({
            "id": treasure[0],
            "name": treasure[1],
            "points": treasure[2]
        })

    return result


@app.route("/players", methods=["POST"])
def add_player():
    data = request.get_json()

    first_name = data["first_name"]
    last_name = data["last_name"]

    db = get_connect()
    cursor = db.cursor()

    cursor.execute("""
        INSERT INTO player (first_name, last_name, score)
        VALUES (?, ?, ?)
    """, (first_name, last_name, 0))

    player_id = cursor.lastrowid

    db.commit()
    db.close()

    return {
        "message": "Player added successfully",
        "player_id": player_id
    }, 201


@app.route("/players/<int:player_id>", methods=["PUT"])
def update_player(player_id):
    data = request.get_json()

    first_name = data["first_name"]
    last_name = data["last_name"]

    db = get_connect()
    cursor = db.cursor()

    cursor.execute("""
        UPDATE player
        SET first_name = ?, last_name = ?
        WHERE id = ?
    """, (first_name, last_name, player_id))

    if cursor.rowcount == 0:
        db.close()
        return {
            "message": "Player not found"
        }, 404

    db.commit()
    db.close()

    return {
        "message": "Player updated successfully"
    }


@app.route("/players/<int:player_id>", methods=["DELETE"])
def delete_player(player_id):
    db = get_connect()
    data = db.cursor()

    data.execute(
        "DELETE FROM player WHERE id = ?",
        (player_id,)
    )

    db.commit()
    db.close()

    return {
        "message": "Player deleted successfully"
    }


if __name__ == "__main__":
    app.run(debug=True)

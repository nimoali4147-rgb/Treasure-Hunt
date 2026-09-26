from database import get_connect
from database import create_player_table


def add_player(first_name, last_name):

    db = get_connect()
    data = db.cursor()

    data.execute("""
        INSERT INTO player (first_name, last_name, score)
        VALUES (?, ?, ?)
    """, (first_name, last_name, 0))

    player_id = data.lastrowid

    db.commit()
    db.close()

    return player_id


def start_game():

    print("TREASURE HUNT")

    first_name = input("\nEnter your first name: ").strip()

    while first_name == "":
        print("First name cannot be empty.")
        first_name = input("Enter your first name: ").strip()

    while last_name == "":
        print("Last name cannot be empty.")
        last_name = input("Enter your last name: ").strip()

    player_id = add_player(
        first_name,
        last_name
    )

    full_name = first_name + " " + last_name

    print("\nWelcome,", full_name + "!")

def main():
        create_player_table
        start_game()

main()
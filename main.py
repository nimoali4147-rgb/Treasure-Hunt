from database import get_connect
from database import create_tables
from database import add_locations
from database import add_treasures  


from game import choose_location
from game import choose_area
from game import search_location


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
        first_name = input(
            "Enter your first name: "
        ).strip()

    last_name = input("Enter your last name: ").strip()

    while last_name == "":
        print("Last name cannot be empty.")
        last_name = input("Enter your last name: ").strip()

    player_id = add_player(
        first_name,
        last_name
    )

    full_name = first_name + " " + last_name

    print("\nWelcome,", full_name )

    selected_location = choose_location()

    selected_area = choose_area(
        selected_location
    )

    search_location(
        player_id,
        selected_location,
        selected_area
    )


def main():

    create_tables()
    add_locations()
    add_treasures()

    start_game()


main()

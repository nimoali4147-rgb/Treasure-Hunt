from database import get_connect
from database import create_tables
from database import add_locations
from database import add_treasures  
from game import choose_location
from game import choose_area
from game import search_location
from treasure import get_score
from treasure import get_score
from treasure import show_treasures


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

def main_menu(player_id,  full_name):
    while True:
        print("\nWhat would you like to do?")
        print("1. Explore another location")
        print("2. View my treasures")
        print("3. View my score")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            selected_location = choose_location()

            selected_area = choose_area(
                selected_location
            )
    
            search_location(
                player_id,
                full_name,
                selected_location,
                selected_area
            )

        elif choice == "2":
            show_treasures(player_id)

        elif choice == "3":
            score = get_score(player_id)

            print("\nMY SCORE")
            print("Current Score:", score)

        elif choice == "4":
            print("\nGAME OVER")
            print("\nThanks for playing Treasure Hunt!")
            break

        else:
            print("\nInvalid choice.")

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
        full_name,
        selected_location,
        selected_area
    )

    main_menu(player_id, full_name)

def main():

    create_tables()
    add_locations()
    add_treasures()

    start_game()


main()

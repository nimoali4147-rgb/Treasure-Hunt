from treasure import find_treasure
from treasure import update_score
from treasure import save_treasure
from treasure import save_history

locations = [
    "Forest",
    "Cave",
    "Island",
    "Desert"
]


areas = {
    "Forest": [
        "Old Tree",
        "River Bank",
        "Abandoned Cabin"
    ],

    "Cave": [
        "Dark Tunnel",
        "Rock Corner",
        "Old Chest"
    ],

    "Island": [
        "Beach",
        "Palm Tree",
        "Shipwreck"
    ],

    "Desert": [
        "Sand Dune",
        "Desert Camp",
        "Ancient Ruins"
    ]
}


def get_number(number):

    while True:

        choice = input(number)

        if choice.isdigit():

            choice = int(choice)
            
            return choice

def choose_location():

    print("\nChoose a location:")

    for i, location in enumerate(locations, start=1):
        print(i, location)

    choice = get_number(
        "Choose a location (1-4): ")
    selected_location = locations[choice - 1]

    print("\nYou entered the", selected_location)

    return selected_location


def choose_area(selected_location):

    print("\nChoose an area to search:")

    selected_areas = areas[selected_location]

    for i, area in enumerate(selected_areas, start=1):
        print(i, area)

    choice = get_number("Choose an area (1-3): ")

    selected_area = selected_areas[choice - 1]

    return selected_area


def search_location(
    player_id,
    player_name,
    selected_location,
    selected_area
):

    print("\nYou searched the", selected_area, "of the", selected_location)

    treasure = find_treasure()

    treasure_id = treasure[0]
    treasure_name = treasure[1]
    points = treasure[2]

    print("\nYou found a treasure!")
    print("Treasure:", treasure_name)
    print("Points: +", points)

    save_treasure(
        player_id,
        treasure_id
    )

    update_score(
        player_id,
        points
    )

    save_history(
    player_id,
    player_name,
    selected_location,
    points,
    treasure_name
    )
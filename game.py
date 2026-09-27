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



def get_number(message):

    while True:

        choice = input(message)

        if choice.isdigit():

            choice = int(choice)

            if 1 <= choice <= 4:
                return choice

        print("Invalid choice. Please enter a number from 1 to 4.")


def choose_location():

    print("\nChoose a location:")

    for i, location in enumerate(locations, start=1):
        print(i, location)

    choice = get_number("Choose a location (1-4): ")

    selected_location = locations[choice - 1]

    print("\nSelected Location:", selected_location)

    return selected_location

def choose_area(selected_location):

    print("\nWhere do you want to search?")

    location_areas = areas[selected_location]

    for i, area in enumerate(location_areas, start=1):
        print(i, area)

    choice = get_number(
        "Choose a place (1-3): ")

    selected_area = location_areas[choice - 1]

    print("\nSearching the", selected_area + "...")

    return selected_area


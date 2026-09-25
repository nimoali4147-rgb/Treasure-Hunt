print("Welcome to Treasure Hunt!")

fist_name = input("Enter your fist name...")
last_name = input("Enter your last name..")

Full_name = fist_name + " " +  last_name

locations = [
    "Forest",
    "Cave",
    "Island",
    "Desert"
]

for i, location in enumerate(locations, start=1):
    print(i, location)

choice = input("choose a location (1-4):")
selected_location = locations[int(choice) - 1]

print("You chose:", selected_location)






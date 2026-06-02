print("VALORANT WEAPONS API MANAGER")
score = 0
weapons= [
    {"name": "vandal", "damage": 160},
    {"name": "ghost", "damage": 80},
    {"name": "operator", "damage": 250}
]
name = input("enter name: ")
def greet():
    print(f"Hello! {name}")  
greet()
def view_weapons():
    for weapon in weapons:
        print(weapon)


def add_weapon():
    weapon_name = input("enter weapon name: ") 
    weapon_damage = int(input("enter weapon damage: "))
    weapon = {
        "name" : weapon_name,
        "damage" : weapon_damage
    }
    weapons.append(weapon)
    print("weapon added successfully")
    print(weapon)
def remove_weapon():
    weapon_name = input("Enter weapon name: ")
    for weapon in weapons:
        if weapon["name"] == weapon_name:
            weapons.remove(weapon)
            print("weapon removed successfully")
            return
    
    print("weapon not found")


import json

def save_weapons():
    with open("weapons.json", "w") as file:
        json.dump(weapons, file)

    print("Weapons saved successfully")
import json
def load_weapons():
        global weapons
        with open("weapons.json", "r") as file:
            json.load(file)

        print("Weapons loaded successfully")
def search_weapon():
    search = input("Search weapon: ")
    for weapon in weapons:
        if weapon["name"] == search:
            print(weapon)
            return
    else: 
        print("weapon unavailable")
def api_lookup():
    import requests

    response = requests.get(
    "https://jsonplaceholder.typicode.com/users"
    )

    users = response.json()

    search_name = input("Enter username: ")

    for person in users:
        if person["username"].lower() == search_name.lower():
            print("Name:", person["name"])
            print("Username:", person["username"])
            print("Phone:", person["phone"])
            print("Email:", person["email"])
            return
     
    print("User not found")
def count_weapons():
    print(len(weapons))

while True:
    print("\n choose an option:")
    menu = ["1. view weapons", "2. add weapons", "3. remove weapons","4. search weapon", "5. save weapons", "6. load weapons", "7. api lookup", "8. count weapons", "9. exit"]
    for item in menu:
        print(item)
    choice = input("Enter choice: ")
    if choice == "1":
        view_weapons()
    elif choice == "2":
        add_weapon()
    elif choice == "3":
        remove_weapon()
    elif choice == "4":
        search_weapon()
    elif choice == "5":
        save_weapons()
    elif choice == "6":
        load_weapons()
    elif choice == "7":
        api_lookup()
    elif choice == "8":
        count_weapons()
    elif choice == "9":
        print("exit")
        break
    else:
        break

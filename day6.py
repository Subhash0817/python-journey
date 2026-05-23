student = {
    "name" : "subhash",
    "age" : "21",
    "course": "cse"
}
print(student ["name"])
print(student ["age"])
student["age"] = 22


student["skills"] = "Python"

print(student)


student ={}
student["name"] = input("enter student name:")
student["age"] = input("enter student age:")
student["course"] = input("enter student course:")

print(student)



player = {
    "username" : "subhash",
    "level" : "21",
    "score" : "30",
    "weapon": "operator"
}
player ["level"] = 90
print(f"Welcome {player['username']}")
print(f"Player level is {player['level']}")
print(f"Player weapon is {player['weapon']}")


player = {}
player["name"] = input("enter user name:")
player["level"] = input("enter user level:")
player["score"] = input("enter user score:")
player["weapon"] = input("enter user weapon:")

print(player)



player = {
    "username" : "subhash",
    "level" : "21",
    "score" : "30",
    "weapon": "operator"
}
for key, value in player.items():
    print(key, ":", value)


player1 = {
    "username" : "subhash",
    "level" : "21",
    "score" : "30",
    "weapon": "operator"
}
player2 = {
    "username" : "v",
    "level" : "23",
    "score" : "30",
    "weapon": "vandal"
}
players =[player1 , player2]
for player in players:
    for key, value in player.items():
        print(key, ":", value)
    print("--------------")



"""NESTED DICTIONARIES"""

players = {
    "player1": {
        "username": "subhash",
        "level": 21,
        "weapon": "operator",
        "score": 90,
        "rank": "platinum",
        "health": 200
            
    },

    "player2": {
        "username": "v",
        "level": 23,
        "weapon": "vandal",
        "score": 90,
        "rank": "diamond",
        "health": 200
    }
}
print(players["player1"]["username"])
print(players["player2"]["level"])
print(players["player1"]["score"])
print(players["player1"].keys())
print(players["player1"].values())




inventory = {
    "gun": {
        "name": "vandal",
        "damage": 160,
        "ammo" : 25,
        "health": 200,
        "price": 2900,
        "rarity": "60%"
            
    },

    "knife": {
        "name": "karambit",
        "damage": 150,
        "ammo": "infinity",
        "health": "infinity",
        "price": "free",
        "rarity": "96%"
    }
}

for weapon, data in inventory.items():
    print(weapon)

    for key, value in data.items():
        print(key, ":", value)

    print("------------")

choice = input("Choose weapon: ")
if choice in inventory:
    print(inventory[choice])
else:
    print("Weapon not found")

print(inventory["gun"]["name"])
print(inventory["knife"]["rarity"])
print(inventory["gun"]["price"])


inventory ={
    "gun": {
            "name": "vandal",
            "damage": 160,
            "ammo" : 25,
            "health": 200,
            "price": 2900,
            "rarity": "60%"
            
        },

            "knife": {
            "name": "karambit",
            "damage": 150,
            "ammo": "infinity",
            "health": "infinity",
            "price": "free",
            "rarity": "96%"
        }
    }

while True:
    print("1. View inventory")
    print("2. Add weapon")
    print("3. Remove weapon")
    print("4. Exit")

    choice = input("Enter choice: ")
    if choice =="1":
        for weapon, data in inventory.items():
            print(weapon)
            for key, value in data.items():
                print(key, ":", value)
                print("-----------")
    elif choice == "2":
        weapon_name = input("Enter weapon name: ")
        damage = input("Enter damage: ")
        ammo = input("Enter ammo: ")

        inventory[weapon_name] = {
            "damage": damage,
            "ammo": ammo
  
}
        file = open("inventory.txt", "a")

        file.write(f"{weapon_name}, {damage}, {ammo}\n")

        file.close()

    elif choice == "3":
        print("Remove weapon")

    elif choice == "4":
        break

    else:
        print("Invalid choice")
weapons = ["vandal", "phantom", "operator"]
weapons.append("ghost")
weapons.remove("phantom")
weapons.insert(1, "knife")
weapons.pop()
weapons.reverse()
weapons.sort()
print(weapons)


weapons = [
    {
        "name": "vandal",
        "damage": 160,
        "ammo": 25
    }
]
while True:
    choice = input("Enter choice: ")
    menu = ["1. view weapon", "2. add weapon", "3. remove weapon", "4. search", "5. exit"]
    for item in menu:
        print(item)
    if choice == "1":
        for weapon in weapons:
            print("Weapon:", weapon["name"])
            print("Damage:", weapon["damage"])
            print("Ammo:", weapon["ammo"])
            print("--------------")
    elif choice == "2":

        weapon_name = input("Enter weapon name: ")
        weapon_damage = input("Enter weapon damage: ")
        weapon_ammo = input("Enter weapon ammo: ")

        weapon = {
        "name": weapon_name,
        "damage": weapon_damage,
        "ammo": weapon_ammo
    }
        weapons.append(weapon)
        print(weapon)
    elif choice == "3":
        weapon_name = input("Enter weapon to remove: ")
        weapons.remove(weapon_name)
    elif choice =="4":
        search = input("Search weapon: ")
        for weapon in weapons:
            if weapon["name"] == search:
                print("weapon available")
            else: 
                print("weapon unavailable")
    elif choice == "5":
        print(exit)
        
    else:
        break


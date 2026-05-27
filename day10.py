weapons = ["vandal", "phantom", "operator"]
weapons.append("ghost")
weapons.remove("phantom")
weapons.insert(1, "knife")
weapons.pop()
weapons.reverse()
weapons.sort()
print(weapons)

weapons = []
while True:
    choice = input("Enter choice: ")
    menu = ["1. view weapon", "2. add weapon", "3. remove weapon", "4. exit"]
    for item in menu:
        print(item)
    if choice == "1":
        for weapon in weapons:
            print(weapon)
    elif choice == "2":
        weapon_name = input("Enter weapon name: ")
        weapons.append(weapon_name)
    elif choice == "3":
        weapon_name = input("Enter weapon to remove: ")
        weapons.remove(weapon_name)
    elif choice =="4":
        print("exit")
    else:
        break

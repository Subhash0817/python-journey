while True:

    print("\n1. Add Note")
    print("2. View Notes")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        note = input("Enter Note: ")

        file = open("notes.txt", "a")

        file.write(note + "\n")

        file.close()

        print("Note Saved")

    elif choice == "2":

        file = open("notes.txt", "r")

        print(file.read())

        file.close()

    elif choice == "3":

        break
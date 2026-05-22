name = input("Enter your name: ")
score = input("Enter your score: ")

file = open("scores.txt", "a")

file.write(f"{name} scored {score}\n")

file.close()

print("Score saved successfully!")
questions = [
    ("What keyword creates a function?", "def"),
    ("Which keyword exits a loop?", "break"),
    ("What function gives string length?", "len")
]

score = 0

for question, answer in questions:
    print(question)

    user_answer = input("Enter answer: ")

    if user_answer == answer:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print(f"Final score: {score}")
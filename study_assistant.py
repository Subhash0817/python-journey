
score = 0
def greet(name):
     print(f"hello {name}")
greet("subhash")
def add(first, second):
        return  first + second
first = int(input("enter first number:"))
second = int(input("enter second number:"))
    
result = add(first, second)
print(result)


def learn_python():
    print("Python is a versatile, high-level programming language known for being incredibly easy to read and write. It is widely used by everyone from beginners to top tech companies like Google and NASA for things like web development, data science, and AI.")

def ai_quiz():
    global score
    print("Quiz starts")
def ask_question(question, correct_answer):
    global score
    print(question)
    answer =input()
    if answer == correct_answer:
                print("correct answer!")
                score += 1
    else:
            print("wrong answer")

while True:
    menu = ["1. learn python", "2.ai quiz", "3.check score", "4.exit"]
    for item in menu:
        print(item)
    choice = input()

    if choice == "1":
        learn_python()
    elif choice == "2":
        ai_quiz()
        ask_question("What keyword creates a function?", "def")

        ask_question("Which keyword exits a loop?", "break")

        ask_question("What function takes user input?", "input")     
    elif choice == "3":
        print(f"🎯 Your current score is: {score}")
    elif choice == "4":
        break
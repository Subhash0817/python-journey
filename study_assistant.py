
score = 0

def learn_python():
    print("Python is a versatile, high-level programming language known for being incredibly easy to read and write. It is widely used by everyone from beginners to top tech companies like Google and NASA for things like web development, data science, and AI.")

def ai_quiz():
    print("Quiz starts")

while True:
    print("1. learn python")
    print("2. AI quiz")
    print("3. check score")
    print("4. exit")

    choice = input()

    if choice == "1":
        learn_python()
    elif choice == "2":
        ai_quiz()
        print("What function gives length of a string?")
        answer =input()
        if answer == "len":
                print("correct answer!")
                score += 1
        else:
            print("wrong answer")
            print("What keyword creates a function?")
            answer =input()
        if answer == "def":
                print("correct answer!")
                score += 1
        else:
            print("wrong answer")
            print("What keyword is used for conditions?")
            answer =input()
        if answer == "if":
                print("correct answer!")
                score += 1
        else:
            print("wrong answer")
            print("Which keyword exits a loop?")
            answer =input()
        if answer == "break":
                print("correct answer!")
                score += 1
        else:
            print("wrong answer")
            print("What function takes user input?")
            answer =input()
        if answer == "input":
                print("correct answer!")
                score += 1
        else:
            print("wrong answer")
            print("What operator checks equality?")
            answer =input()
        if answer == "==":
                print("correct answer!")
                score += 1
        else:
            print("wrong answer")
            print("Which loop runs while condition is True?")
            answer =input()
        if answer == "while":
                print("correct answer!")
                score += 1
        else:
            print("wrong answer")
            print("What does AI stand for?")
            answer =input()
        if answer == "artificial intelligence":
                print("correct answer!")
                score += 1
        else:
            print("wrong answer")
            print("What language is most used in AI?")
            answer =input()
        if answer == "python":
                print("correct answer!")
                score += 1
        else:
            print("wrong answer")
            print("What does LLM stand for?")
            answer =input()
        if answer == "large language model":
                print("correct answer!")
                score += 1
        else:
            print("wrong answer") 
    elif choice == "3":
        print(f"🎯 Your current score is: {score}")
    elif choice == "4":
        break
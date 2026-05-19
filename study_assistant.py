score = 0
while True:

    print("1. learn python")
    print("2. Ai qiz")
    print("3. check score")
    print("4. exit")

    choice = input()
    if choice =="1":
        print("Python is a high-level, general-purpose programming language known for its simple, readable syntax that resembles the English language. Originally created by Guido van Rossum in 1991, it is designed to let developers express concepts with fewer lines of code than languages like C++ or Java")
    elif choice == "2":
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
        print(f"🎯 Your current score is: {score}")
    elif choice =="3":
        print(f"Your current score is {score}")
    elif choice =="4":
        print("Exiting")
        break
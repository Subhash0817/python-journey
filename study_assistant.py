score = 0
while True:

    print("1. learn python")
    print("2. Ai qiz")
    print("3. exit")

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
        print(f"Your score is {score}")
    elif choice =="3":
        print("Exiting")
        break
   
while True:
    try:
        first_number = int(input("enter a number:"))
        second_number = int(input("enter a number:"))
        print(first_number / second_number)

        break

    except ValueError:
        print("please enter numbers only")
    except ZeroDivisionError:
        print("cannot divide by zero")
def add(first, second):
    return  first + second
def sub(first, second):
            return  first - second
def div(first, second):
            return  first / second
def mul(first, second):
            return  first * second
while True:
    try:

        print("\nChoose an option:")
        menu = ["1. add", "2. subtract", "3. division", "4.multiply", "5. exit"]
        for item in menu:
            print(item)
        choice = input()
        if choice == "1":
            first = int(input("Enter first number: "))
            second = int(input("Enter second number: "))
            print(add(first, second))
        elif choice == "2":
            first = int(input("enter first number:"))
            second = int(input("enter second number:"))
    
            result = sub(first, second)
            print(result)
        elif choice =="3":
            first = int(input("enter first number:"))
            second = int(input("enter second number:"))
    
            result = div(first, second)
            print(result)
        elif choice =="4":
            first = int(input("enter first number:"))
            second = int(input("enter second number:"))
            result = mul(first, second)
            print(result)       
        elif choice == "5":
              print("Thanks for using safe calculator!")
              break
        else:
              print("invalid choice")
    
    except ValueError:
        print("Please enter numbers only")

    except ZeroDivisionError:
        print("Cannot divide by zero")
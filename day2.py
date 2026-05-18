"""def say_name():
    print("subhash")

say_name()


first_number = int(input("enter a:"))
second_number = int(input("enter b:"))
def add_numbers():

    print(first_number+second_number)

add_numbers()"""

number = int(input("enter a number:"))
def is_even(number):
    if number % 2== 0:
        return True
    else:
        return False
    
if is_even(number):
    print("it is even")
else:
    print("its odd")

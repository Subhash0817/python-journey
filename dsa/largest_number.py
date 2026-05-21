numbers =[ 4, 3, 5, 6, 2, 9]
largest = numbers[0]
for number in numbers:
    if number > largest:
        largest = number
user = int(input("Guess the largest number: "))

if user == largest:
    print("Correct guess!")
else:
    print("Wrong guess!")

print(f"The largest number was {largest}")


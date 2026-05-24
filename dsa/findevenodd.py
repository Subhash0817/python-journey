numbers = [4, 7, 2, 9, 10, 13, 8]
even_numbers = []
odd_numbers =[]
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
print(even_numbers)
for number in numbers:
    if number % 2 != 0:
        odd_numbers.append(number)
print(odd_numbers)

numbers = [4, 7, 2, 9, 10, 13, 8]
even_numbers = []
odd_numbers =[]

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)
print(even_numbers)
print(odd_numbers)
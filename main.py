from maths_utils import add, sub, mul

print(add(5, 3))
print(sub(10, 2))
print(mul(4, 6))


import maths_utils
print(maths_utils.add(5, 3))
print(maths_utils.sub(10, 2))


import random
number = random.randint(1,10)
attempts = 0
while True:
    guess = int(input("guess a number: "))
    attempts += 1
    if guess == number:
        print("correct")
        print(f"You guessed in {attempts} attempts")
        break
    elif guess > number:
        print("too high")
       
    else:
        print("too low")
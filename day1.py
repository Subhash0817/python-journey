name = input("enter your name: ")
age = int(input("enter your age: "))
city = input("enter your city: ")

print(f"Hello {name}!")
print(f"You are {age} years old.")
print(f"You live in {city}.")

print(name.upper())
print(len(name))
print("a" in(name))

student = input("enter student name:")
marks = int(input("enter marks:"))

if (marks >= 90):
   grade = "A"
elif(marks>= 75  ):
    grade = "B"
elif (marks>= 60):
    grade = "C"
elif (marks>= 40):
     grade= "D"

else:
    print("F")  
  
print(f"{student} got grade {grade} ")




password= input("enter password:")
if len(password) >8:
    print("strong password")
else:
    print("weak password")


number = int(input("enter number:"))
for i in range(1,11):
    print(f"{number}*{i} = {number*i}")

number = 0
for i in range(1,6):
    number += i
print(number)



text = input("enter text:")
count = 0
for letter in text:
    if letter in "a e i o u":
        count+= 1
print(f"vowels:{count}")



for i in range (1,101):
    print(i)


for i in range (2,100,2):
    print(i)

city =input("enter city name:")
print(len(city))

text = input("enter the text:")

if text == text[::-1]:
    print("palindrome")
else:
    print("not a palindrome")




guess_value = int(input("can u guess?:"))
secret_value =9
while guess_value != secret_value:
    print("wrong, try again")
    guess_value = int(input("can u guess again?:"))

print("Congrats! Right answer!")
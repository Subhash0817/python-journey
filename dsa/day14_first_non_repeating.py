user = input("enter a string: ")
count = {}
for char in user:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1
found = False
print(count)
for char in user:
    if count[char] == 1:
        print("The non-repeating character:", char)
        found = True
        break
if not found:
    print("No non-repeating character found")
def count_vowels():
   
    word = input("enter text:")
    count = 0
    for letter in word:
        if letter in "aeiou":
            count+= 1
    print(f"vowels:{count}")

count_vowels()

def palindrome():
    word = input("enter text:")
    reversed_word = ""
    for letter in word:
        reversed_word = letter + reversed_word
    if word == reversed_word:
        print("it is a palindrome")
    else:
        print("not palindrome")
palindrome()

def count_words():
    word = input("enter text:")
    count = 0
    for letter in word:
        count += 1
    print(count)
count_words()


def remove_spaces():
    word = input("enter text:")
    new_word = ""
    for letter in word:
        if letter != " ":
            new_word += letter
    print(new_word)
remove_spaces()
#Vowel Eater program version 3 by removing redundant if elif statements
user_word = input('Enter a word: ')
user_word = user_word.upper()
vowels = ['a','e','i','o','u']

for letter in user_word:
    if letter.lower() not in vowels:
        print(letter)


user_word = input('Enter a word: ')
user_word = user_word.upper()

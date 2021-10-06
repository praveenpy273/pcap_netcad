# The program ask the user to enter a word;
# use user_word = user_word.upper() to convert the word entered by the user to upper case
# use conditional execution and the continue statement to "eat" the following vowels A, E, I, O, U from the inputted word;
# print the uneaten letters to the screen, each one of them on a separate line
# using for loop;(if-elif-else) and the continue statement.



user_word = input('Enter a word: ')
user_word = user_word.upper()

for letter in user_word:
    if letter.lower() == 'a':
      continue
    elif letter.lower() == 'e':
      continue
    elif letter.lower() == 'i':
      continue
    elif letter.lower() == 'o':
      continue
    else:
        print(letter)

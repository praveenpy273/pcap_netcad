# Program must ask the user to enter a word;
# use user_word = user_word.upper() to convert the word entered by the user to upper case
# use conditional execution and the continue statement to "eat" the following vowels A, E, I, O, U from the inputted word;
# assign the uneaten letters to the word_without_vowels variable and print the variable to the screen.
# using for loop, (if-elif-else),the continue statement.

word_without_vowels = ''
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
    elif letter.lower() == 'u':
      continue
    else:
        word_without_vowels += '' + letter
    print(word_without_vowels)

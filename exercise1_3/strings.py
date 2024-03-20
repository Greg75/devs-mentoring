import random


# ---------- Exercise number 1 ----------
print('Exercise number 1')
# Collecting text from the user
text = input("Type any text with at least 7 characters: ")

# Assessing length, first and last character of the given text
length = len(text)
first_char = text[0]
last_char = text[-1]

# Setting random number for 3-letter substring
random_char = random.randint(0, length - 3)

# Printing text, its length, first, last character and 3-letter substring
print(text)
print(f'The length of the given text is: {length} characters.')
print(f'First character of the given text is: {first_char}, last character is: {last_char}.')
print(f'Random, next three characters: {text[random_char:random_char + 3]}.')


# ---------- Exercise number 2 ----------
print('\n')
print('Exercise number 2')
# Collecting number of cats given by user
cats_number = int(input('How many cats does Ala have: '))
print('Today Ala has found next 3 cats in "baby hatch".')

# Adding 3 cats to the number of cats given by user and printing total number on the screen
cats_number += 3
cats_breeding = f'Now Ala has {cats_number} cats.'
print(cats_breeding)

# Displaying all words separated by comma
print(cats_breeding.replace(' ', ','))

# Printing each word on a single line
cats_breeding_split = cats_breeding.split(' ')
print(cats_breeding_split[0])
print(cats_breeding_split[1])
print(cats_breeding_split[2])
print(cats_breeding_split[3])
print(cats_breeding_split[4])

# Or using for loop
# for word in cats_breeding.split(' '):
#     print(f'{word}')

# Checking if all the letters in a statement are lowercase and printing the statement all in lowercase letter
if cats_breeding.islower():
    print(cats_breeding)
else:
    print(cats_breeding.lower())

# Setting the first letter as a capital one and printing the result
print(cats_breeding.capitalize())


# ---------- Exercise number 3 ----------
print('\n')
print('Exercise number 3')
text = 'DOM'
print(text.lower() + 'ek')


# ---------- Exercise number 4 ----------
print('\n')
print('Exercise number 4')
text = input('Type any text: ')
print(text.upper())


# ---------- Exercise number 5 ----------
print('\n')
print('Exercise number 5')
text = input('Type any text prefixed by 5 spaces: ')
print(text)
print(text.lstrip())


# ---------- Exercise number 6 ----------
print('\n')
print('Exercise number 6')
colors = 'black,white,red,green,blue'
colors_split = colors.split(',')
print(colors_split[2])

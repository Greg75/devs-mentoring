import random

# ---------- Exercise number 1 ----------
print('Exercise number 1')
text = input('Type any text: ')
for i in range(10):
    print(text, end=' ')


# ---------- Exercise number 2 ----------
print('Exercise number 2')
number = int(input('Type any number: '))
total = 0
for i in range(1, number + 1):
    total += i
print(f'Total sum: {total}')


# ---------- Exercise number 3 ----------
print('Exercise number 3')
numbers = []
for i in range(1, 11):
    number = int(input(f'Type number {i} out of 10: '))
    numbers.append(number)

for number in numbers:
    if number % 2 == 0:
        print(number)


# ---------- Exercise number 4 ----------
print('Exercise number 4')
weekdays = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
weekday = int(input('Type day number: '))
if weekday not in weekdays.keys():
    print('There is no such day! Try again.')
else:
    print(f'Chosen day: {weekdays[weekday]}.')


# ---------- Exercise number 5 ----------
print('Exercise number 5')
d = (1, [2, 4], 'tekst', 3 + 5j)
print(f'Tuple\'s last element: {d[-1]}.')
print(f'Tuple\'s first and second element: {d[:2]}.')
if 'abc' in d:
    print("'abc' is an element of the tuple.")
else:
    print("'abc' is not an element of the tuple.")


# ---------- Exercise number 6 ----------
print('Exercise number 6')
a = [3, 1, 5, 7, 9, 2, 6]
print(f'Fourth element of the list: {a[3]}')
print(f'Element two up to four: {a[1:4]}')
print(f'From the fourth element to the end of the list: {a[3:]}')
print(f'From the third last element to the end of the list: {a[-3:]}')
print(f'From the first element up to the fourth element exclusive: {a[:3]}')
print(f'From the fourth element to the last element: {a[3:-1]}')
print(f'Every second element starting from the first one: {a[::2]}')
print(f'Starting from sixth element up to the third element exclusive, with step -1: {a[5:2:-1]}')
print(f'Sum: {sum(a)}')
print(x := '8' in a)
print(y := '4' not in a)


# ---------- Exercise number 7 ----------
print('Exercise number 7')
number = int(input('Type any integer number: '))
if number >= 0:
    print(number)
else:
    print(number * -1)


# ---------- Exercise number 8 ----------
print('Exercise number 8')
weight_categories = ['underweight', 'normal weight', 'light overweight', 'heavy overweight']
weight = int(input('Type your weight in kg: '))
height = float(input('Type your height in meters: '))
bmi = weight / height ** 2
if bmi < 18.5:
    print('You are underweight.')
elif 18.5 <= bmi <= 24:
    print('You are normal weight.')
elif 24 < bmi <= 26.5:
    print('You are slightly overweight.')
elif bmi > 26.5:
    if 30 <= bmi <= 35:
        print('You are overweight and have obesity 1st level.')
    elif 35 < bmi <= 40:
        print('You are overweight and have obesity 2nd level.')
    elif bmi > 40:
        print('You are overweight and have obesity 3rd level.')
    else:
        print('You are overweight.')


# ---------- Exercise number 9 ----------
print('Exercise number 9')
print(True and False)  # False - conjunction
print(True and True)  # True - conjunction
print(False or False)  # False - alternative
print(False or True)  # True - alternative


# ---------- Exercise number 10 ----------
print('Exercise number 10')
lower_limit = int(input('Type number of lower limit: '))
upper_limit = int(input('Type number of upper limit: '))
draw_number = random.randint(lower_limit, upper_limit)
player_number = None
scores = upper_limit - lower_limit
while player_number != draw_number:
    player_number = int(input('Guess a number: '))
    if player_number < draw_number:
        print('Your number is too low.')
    elif player_number > draw_number:
        print('Your number is too high.')
    scores -= 1
else:
    print(f'Congrats! You gained {scores} scores.')


# ---------- Exercise number 11 ----------
print('Exercise number 11')
print('Rectangle 7x6:')
for i in range(6):
    for j in range(7):
        print('*', end='')
    print()


print('Square 5x5:')
for i in range(5):
    if i == 0 or i == 4:
        print('*' * 5)
    else:
        print('*' + ' ' * 3 + '*')

print('Tree height of 5:')
for i in range(5):
    print(' ' * (5 - (i + 1)), '*' * (2 * i + 1))


# ---------- Exercise number 12 ----------
print('Exercise number 12')
for i in range(97, 123):
    print(chr(i), end=' ')

print()

for i in range(90, 64, -1):
    print(chr(i), end=' ')


# ---------- Exercise number 13 ----------
print('Exercise number 13')
words_dict = {}
while True:
    print()
    print('Your personal dictionary:')
    print('-' * 20)
    print('1. Add word with definition')
    print('2. Find word\'s definition')
    print('3. Delete word with its definition')
    print('4. Exit program')
    print('-' * 20)
    user_choice = int(input('Type your choice: '))
    if user_choice == 4:
        print('Bye, bye')
        break
    elif user_choice == 1:
        word = input('Type a word: ')
        definition = input('Type a definition of the word: ')
        words_dict.update({word: definition})
        print(words_dict)
    elif user_choice == 2:
        word = input('Type a word which you are looking for: ')
        print(f'{word} definition: {words_dict.get(word, "This word does not exist in that dictionary.")}')
    elif user_choice == 3:
        word = input('Type a word to delete: ')
        words_dict.pop(word)
        print(words_dict)
    else:
        print('Wrong choice. Try again.')


# ---------- Exercise number 14 ----------
print('Exercise number 14')
factor = int(input('Type size of the plus sign /odd number/: '))
size = range(factor)
plus = [[' ' * (len(size) // 2) + '*' + ' ' * (len(size) // 2)], ['*' * len(size)]]

if len(size) % 2 == 0:
    print('Incorrect size. Size has to be odd number.')
else:
    for i in size:
        if (len(size) // 2) == i:
            print(plus[1])
        else:
            print(plus[0])


# ---------- Exercise number 15 ----------
print('Exercise number 15')
persons = {
    '02011210075': {'eyes_color': 'green', 'firstname': 'Bob', 'lastname': 'Twain', 'age': 22},
    '00102408862': {'eyes_color': 'blue', 'firstname': 'Jack', 'lastname': 'Teacher', 'age': 24},
    '98062104624': {'eyes_color': 'grey', 'firstname': 'Tom', 'lastname': 'Cruise', 'age': 26},
    '90041608435': {'eyes_color': 'green', 'firstname': 'Eva', 'lastname': 'Minge', 'age': 34},
    '88022944071': {'eyes_color': 'yellow', 'firstname': 'Marie', 'lastname': 'Tuscon', 'age': 36},
}

print(f'The chosen person\'s eyes are {persons["98062104624"]["eyes_color"]}')

# Adding random mother's name to each person
mother_names = ['Lola', 'Kate', 'Victoria', 'Sophia', 'Shakira']
for i, person in enumerate(persons):
    persons[person].update({'mother_name': mother_names[random.randint(0, len(mother_names) - 1)]})

# Deleting person who's PESEL is ended with number 1
for person in persons.copy():
    if person[-1] == '1':
        persons.pop(person)

# Printing people with friendly form
for person in persons:
    print(f'PESEL: {person}')
    for k, v in persons[person].items():
        print(f'{k}: {v}')
    print()

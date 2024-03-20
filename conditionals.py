import random
import time

# ---------- Exercise number 1 ----------
print('Exercise number 1')
side_names = ['A', 'B', 'C']
side_lengths = []

for side_name in side_names:
    side_length = int(input(f'Type length of side {side_name}: '))
    side_lengths.append(side_length)

side_lengths.sort()

if (side_lengths[0] ** 2) + (side_lengths[1] ** 2) == side_lengths[-1] ** 2:
    print('This is right triangle!')
else:
    print('It is not right triangle. Try again.')


# ---------- Exercise number 2 ----------
print('Exercise number 2')
number = int(input('Type any number: '))
if number < 0:
    print('This is negative number.')
elif number > 0:
    print('This is positive number.')
else:
    print('This is zero.')


# ---------- Exercise number 3 ----------
print('Exercise number 3')
numbers = []
for i in range(3):
    number = int(input(f'Type number {i + 1} out of 3: '))
    numbers.append(number)

print(f'The highest number is: {max(numbers)}.')


# ---------- Exercise number 4 ----------
print('Exercise number 4')
tools = ['scissors', 'stone', 'paper']
player1_tool = input('Player 1 choice is: ')
player2_tool = input('Player 2 choice is: ')
if player1_tool not in tools or player2_tool not in tools:
    print('Incorrect data. Try again.')
elif player1_tool == player2_tool:
    print('It\'s a draw!')
elif (player1_tool == 'scissors' and player2_tool == 'stone') or \
        (player1_tool == 'stone' and player2_tool == 'paper') or \
        (player1_tool == 'paper' and player2_tool == 'scissors'):
    print('Player 2 won!')
elif (player1_tool == 'scissors' and player2_tool == 'paper') or \
        (player1_tool == 'stone' and player2_tool == 'scissors') or \
        (player1_tool == 'paper' and player2_tool == 'stone'):
    print('Player 1 won!')


# ---------- Exercise number 5 ----------
print('Exercise number 5')
numbers = []
even_numbers = []
for i in range(2):
    number = int(input(f'Type number {i + 1} out of 2: '))
    numbers.append(number)

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        continue

if len(even_numbers) != 0:
    print('At least one given number is even.')
else:
    print('There was no even numbers given.')


# ---------- Exercise number 6 ----------
print('Exercise number 6')
user_score, computer_score = 0, 0

while True:
    user_choice = input('Type "h" for heads or "t" for tails: ')
    if user_choice == "h":
        user_choice = 1
    elif user_choice == "t":
        user_choice = 0
    else:
        print('Incorrect data.')

    for second in range(3, -1, -1):
        if second == 0:
            print('Tossing the coin...')
            computer_choice = random.randint(0, 1)
            coin_toss = random.randint(0, 1)
            if coin_toss == 0:
                print('Result is: Tails!')
            else:
                print('Result is: Heads!')
            if user_choice == coin_toss:
                user_score += 1
            elif computer_choice == coin_toss:
                computer_score += 1
            print(f'User scores: {user_score}, computer scores: {computer_score}.')
        else:
            print(f'{second}...', end=' ')
            time.sleep(0.5)

    play_game = input('Do you want to continue? (y/n): ')
    if play_game == 'y':
        continue
    elif play_game == 'n':
        break

# ---------- Exercise number 1 ----------
print('Exercise number 1')
end_of_range = int(input('Type end of range numbers: '))

# For loop in use
print('For Loop:')
for number in range(end_of_range + 1):
    print(number)

# While loop in use
number = 0
print('While Loop:')
while number <= end_of_range:
    print(number)
    number += 1


# ---------- Exercise number 2 ----------
print('Exercise number 2')

# For loop in use
print('For Loop:')
for number in range(100, 49, -1):
    print(number)

# While loop in use
number = 100
print('While Loop:')
while number >= 50:
    print(number)
    number -= 1


# ---------- Exercise number 3 ----------
print('Exercise number 3')
for number in range(0, 101, 5):
    print(number)


# ---------- Exercise number 4 ----------
print('Exercise number 4')
power_count = int(input('Type number of consecutive power of 2: '))
for power in range(power_count):
    print(f'2 to the {power} power = {2 ** power}')


# ---------- Exercise number 5 ----------
print('Exercise number 5')
start_range = int(input('Type start range number: '))
end_range = int(input('Type end range number: '))
factor = int(input('Type factor: '))
divisible_numbers = []
for number in range(start_range, end_range):
    if number % factor == 0:
        divisible_numbers.append(number)
    else:
        continue

print(f'The list of numbers divisible by {factor}: {divisible_numbers}.')


# ---------- Exercise number 6 ----------
print('Exercise number 6')
total = 0
while True:
    number = int(input('Type any number: '))
    if total + number > total:
        total += number
    else:
        total += number
        break
print(f'Sum of the numbers: {total}.')


# ---------- Exercise number 7 ----------
print('Exercise number 7')

# Pattern
print('Pattern:')
print('*' * 10)

# Right triangle of height 4
print('Right triangle:')
for i in range(1, 5):
    print('*' * i)

# Square 3x3
print('Square 3x3:')
for i in range(3):
    print('*' * 3)

# Tree
print('Tree:')
for i in range(1, 10, 2):
    branch = '*' * i
    print(branch.center(9))


# ---------- Exercise number 8 ----------
print('Exercise number 8')
total = 0
for number in range(11):
    total += number

print(f'Arithmetic mean of first 10 natural numbers: {total / 10}.')


# ---------- Exercise number 9 ----------
print('Exercise number 9')
fuel = 0
astronauts = 0
altitude = 0

while not 5000 <= fuel <= 30000:
    fuel = int(input('Type initial fuel load: '))
    if 5000 <= fuel <= 30000:
        print(f'Initial fuel load: {fuel} l.')
    else:
        print('Incorrect fuel load. Try again.')
        continue

while not 0 < astronauts <= 7:
    astronauts = int(input('Type number of astronauts: '))
    if 0 < astronauts <= 7:
        print(f'Astronauts number: {astronauts}.')
    else:
        print('Incorrect astronauts number. Try again.')

spaceship_fuel_consumption_per_100km = 300 + 100 * astronauts
min_fuel_level = spaceship_fuel_consumption_per_100km
while fuel > min_fuel_level:
    altitude += 100
    fuel -= 300 + 100 * astronauts
    print(f'Spaceship traveled {altitude} km.')

if altitude > 2000:
    print('Spaceship reached the orbit.')
else:
    print('Spaceship didn\'t reached the orbit.')


# ---------- Exercise number 10 ----------
print('Exercise number 10')
divisors = []
number = int(input('Type any number: '))
for divisor in range(1, number):
    if number % divisor == 0:
        divisors.append(divisor)

if sum(divisors) == number:
    print('Given number is a perfect number!')
else:
    print('Given number is not a perfect number.')

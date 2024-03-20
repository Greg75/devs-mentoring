# ---------- Exercise number 1 ----------
print('Exercise number 1')
for i in range(1, 10):
    if i < 6:
        print('*' * i)
    else:
        print('*' * (10 - i))


# ---------- Exercise number 2 ----------
print('Exercise number 2')
word = input('Type a word: ')
is_palindrome = ''
if word.lower() == word[::-1].lower():
    print(f'This is palindrome.')
else:
    print('This is not palindrome!')


# ---------- Exercise number 3 ----------
print('Exercise number 3')
persons = ['Adam', 'Stanisław', 'Joanna', 'Kornelia', 'Kacper']

# Solution number 1
for person in persons:
    for i in range(len(persons)):
        if person == persons[i]:
            continue
        else:
            print(f'{person} - {persons[i]}')
    print()

# Solution number 2
for person in persons:
    i = persons.index(person)
    relatives = persons[i + 1:]
    for relative in relatives:
        print(f'{person} - {relative}')
    print()

# ---------- Exercise number 4 ----------
print('Exercise number 4')
for number in range(1000, 10000):
    print(number)


# ---------- Exercise number 5 ----------
print('Exercise number 5')
order = {
    'Client_1335': {'dish name': 'chicken soup', 'grade': 5, 'recipe': 20.0},
    'Client_222': {'dessert name': 'vanilla ice cream', 'recipe': 5.0}
}

for client in order.keys():
    print()
    print(f'{client}:')
    for k, v in order[client].items():
        print(f'{k}: {v}')


# ---------- Exercise number 6 ----------
print('Exercise number 6')
counter = {}
number = input('Type any integer number: ')
for digit in number:
    if digit not in counter.keys():
        counter.update({digit: 1})
    else:
        counter[digit] += 1
print(counter)


# ---------- Exercise number 7 ----------
print('Exercise number 7')
fibonacci_array = []
number = int(input('Type number of elements of Fibonacci array: '))

n, n1 = 0, 0
for _ in range(number):
    if len(fibonacci_array) < 1:
        fibonacci_array.append(n)
        n = 1
    else:
        n2 = n1 + n
        n = n1
        n1 = n2
        fibonacci_array.append(n2)

print(f'Fibonacci numbers: {fibonacci_array}.')
